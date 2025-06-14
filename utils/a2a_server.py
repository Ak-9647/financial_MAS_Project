import uvicorn
import json
import uuid
from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import JSONResponse
from typing import Dict

class TaskManager:
    """A simple in-memory task manager for demonstration."""
    def __init__(self, agent):
        self.agent = agent
        self.tasks: Dict[str, dict] = {}

    async def create_and_run_task(self, request: dict) -> dict:
        task_id = str(uuid.uuid4())
        initial_message = request["message"]
        task = {
            "id": task_id, 
            "state": "WORKING", 
            "messages": [initial_message]
        }
        self.tasks[task_id] = task

        try:
            # Extract the payload from the message
            payload_text = initial_message["parts"][0]["text"]
            payload = json.loads(payload_text)
            
            # Execute the actual agent
            result_content = await self.agent.execute(payload)
            
            final_message = {
                "role": "agent", 
                "parts": [{"text": json.dumps(result_content)}]
            }
            task["messages"].append(final_message)
            task["state"] = "COMPLETED"
        except Exception as e:
            error_message = f"Error during agent execution: {e}"
            task["state"] = "ERRORED"
            task["messages"].append({
                "role": "agent", 
                "parts": [{"text": error_message}]
            })
        
        self.tasks[task_id] = task
        return task

    def get_task(self, task_id: str) -> dict | None:
        return self.tasks.get(task_id)

class A2AServer:
    """An A2A compliant server that wraps an ADK agent."""
    def __init__(self, host, port, agent, agent_card):
        self.app = Starlette(debug=True)
        self.task_manager = TaskManager(agent)
        self.agent_card = agent_card
        self.host = host
        self.port = port
        self.app.add_route("/", self.handle_a2a_request, methods=["POST"])
        self.app.add_route("/.well-known/agent.json", self.serve_agent_card, methods=["GET"])

    async def serve_agent_card(self, request: Request) -> JSONResponse:
        return JSONResponse(self.agent_card)

    async def handle_a2a_request(self, request: Request) -> JSONResponse:
        body = await request.json()
        try:
            task = await self.task_manager.create_and_run_task(body)
            return JSONResponse(task)
        except Exception as e:
            return JSONResponse({"error": "Invalid A2A request", "details": str(e)}, status_code=400)

    def run(self):
        uvicorn.run(self.app, host=self.host, port=self.port) 