import uvicorn
import json
import uuid
from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.middleware.cors import CORSMiddleware
from typing import Dict

class ADKTaskManager:
    """Enterprise ADK task manager with enhanced capabilities."""
    def __init__(self, adk_agent):
        self.adk_agent = adk_agent
        self.tasks: Dict[str, dict] = {}

    async def create_and_run_task(self, request: dict) -> dict:
        task_id = str(uuid.uuid4())
        initial_message = request["message"]
        task = {
            "id": task_id, 
            "state": "WORKING", 
            "messages": [initial_message],
            "adk_metadata": {
                "agent_name": self.adk_agent.name,
                "agent_id": getattr(self.adk_agent, 'agent_id', 'unknown'),
                "adk_version": getattr(self.adk_agent, 'adk_version', '1.0'),
                "capabilities": getattr(self.adk_agent, 'capabilities', [])
            }
        }
        self.tasks[task_id] = task

        try:
            # Extract the payload from the message
            payload_text = initial_message["parts"][0]["text"]
            if isinstance(payload_text, str):
                try:
                    payload = json.loads(payload_text)
                except json.JSONDecodeError:
                    # If it's not valid JSON, treat it as a simple string query
                    payload = {"query": payload_text}
            else:
                payload = payload_text
            
            # Execute the ADK agent with enterprise features
            result_content = await self.adk_agent.execute(payload)
            
            final_message = {
                "role": "agent", 
                "parts": [{"text": json.dumps(result_content)}]
            }
            task["messages"].append(final_message)
            task["state"] = "COMPLETED"
            task["adk_execution_complete"] = True
        except Exception as e:
            error_message = f"ADK agent execution error: {e}"
            task["state"] = "ERRORED"
            task["messages"].append({
                "role": "agent", 
                "parts": [{"text": error_message}]
            })
            task["adk_error"] = True
        
        self.tasks[task_id] = task
        return task

    def get_task(self, task_id: str) -> dict | None:
        return self.tasks.get(task_id)

class A2AServer:
    """An A2A compliant server that wraps an ADK agent with enterprise features."""
    def __init__(self, host, port, adk_agent, agent_card):
        self.app = Starlette(debug=True)
        
        # Add CORS middleware for enterprise frontend integration
        self.app.add_middleware(
            CORSMiddleware,
            allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )
        
        self.task_manager = ADKTaskManager(adk_agent)  # Enhanced ADK task manager
        self.agent_card = agent_card
        self.host = host
        self.port = port
        self.adk_agent = adk_agent  # Store ADK agent reference
        
        # ADK-enhanced routing
        self.app.add_route("/", self.handle_adk_request, methods=["POST"])
        self.app.add_route("/.well-known/agent.json", self.serve_adk_agent_card, methods=["GET"])
        self.app.add_route("/adk/info", self.get_adk_info, methods=["GET"])  # New ADK endpoint
        self.app.add_route("/adk/capabilities", self.get_adk_capabilities, methods=["GET"])  # New ADK endpoint

    async def serve_adk_agent_card(self, request: Request) -> JSONResponse:
        """Serve enhanced ADK agent card with enterprise metadata"""
        enhanced_card = {
            **self.agent_card,
            "adk_enhanced": True,
            "adk_version": getattr(self.adk_agent, 'adk_version', '1.0'),
            "enterprise_features": True,
            "capabilities": getattr(self.adk_agent, 'capabilities', []),
            "agent_state": getattr(self.adk_agent, 'state', 'unknown')
        }
        return JSONResponse(enhanced_card)

    async def handle_adk_request(self, request: Request) -> JSONResponse:
        """Handle ADK-enhanced A2A requests with enterprise features"""
        body = await request.json()
        try:
            task = await self.task_manager.create_and_run_task(body)
            return JSONResponse(task)
        except Exception as e:
            return JSONResponse({
                "error": "Invalid ADK A2A request", 
                "details": str(e),
                "adk_error": True
            }, status_code=400)
    
    async def get_adk_info(self, request: Request) -> JSONResponse:
        """Get comprehensive ADK agent information"""
        if hasattr(self.adk_agent, 'get_adk_info'):
            return JSONResponse(self.adk_agent.get_adk_info())
        else:
            return JSONResponse({
                "name": getattr(self.adk_agent, 'name', 'Unknown'),
                "adk_version": getattr(self.adk_agent, 'adk_version', '1.0'),
                "state": getattr(self.adk_agent, 'state', 'unknown'),
                "capabilities": getattr(self.adk_agent, 'capabilities', [])
            })
    
    async def get_adk_capabilities(self, request: Request) -> JSONResponse:
        """Get ADK agent capabilities"""
        if hasattr(self.adk_agent, 'get_capabilities'):
            return JSONResponse({"capabilities": self.adk_agent.get_capabilities()})
        else:
            return JSONResponse({"capabilities": getattr(self.adk_agent, 'capabilities', [])})

    def run(self):
        uvicorn.run(self.app, host=self.host, port=self.port) 