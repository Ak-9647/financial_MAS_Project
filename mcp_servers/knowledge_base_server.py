import uvicorn
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.simple_mcp import FastMCP
from services.knowledge_service import ChromaDBService
from starlette.applications import Starlette
from starlette.routing import Route
from starlette.responses import JSONResponse

mcp = FastMCP("Knowledge Base Server")
kb_service = ChromaDBService()

@mcp.tool()
def query_vector_db(query: str) -> list:
    """Searches the financial knowledge base for information relevant to the query."""
    return kb_service.query(query)

# Create simple web server for MCP tools
async def handle_tool_request(request):
    body = await request.json()
    tool_name = body.get('tool')
    params = body.get('params', {})
    
    try:
        result = mcp.call_tool(tool_name, **params)
        return JSONResponse({"result": result})
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=400)

async def list_tools(request):
    tools = mcp.get_tools()
    tool_list = [{"name": name, "description": info['description']} for name, info in tools.items()]
    return JSONResponse({"tools": tool_list})

app = Starlette(routes=[
    Route('/tools', list_tools, methods=["GET"]),
    Route('/call', handle_tool_request, methods=["POST"]),
])

if __name__ == "__main__":
    print("Populating DB if necessary...")
    kb_service.populate_db_if_empty()
    print("Starting Knowledge Base MCP Server on port 8003...")
    uvicorn.run(app, host="0.0.0.0", port=8003) 