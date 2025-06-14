import uvicorn
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.simple_mcp import FastMCP
from services.web_research_service import SerperDevService
from starlette.applications import Starlette
from starlette.routing import Route
from starlette.responses import JSONResponse

mcp = FastMCP("Web Research Server")
web_service = SerperDevService()

@mcp.tool()
def search_google(query: str, n_results: int = 5) -> list:
    """Performs a Google search for the given query and returns the top results."""
    return web_service.search_google(query, n_results)

@mcp.tool()
def get_text_from_page(url_to_scrape: str) -> str:
    """Scrapes and returns the text content from a given URL."""
    return web_service.get_text_from_page(url_to_scrape)

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
    print("Starting Web Research MCP Server on port 8002...")
    uvicorn.run(app, host="0.0.0.0", port=8002) 