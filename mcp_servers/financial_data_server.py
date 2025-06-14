import uvicorn
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.simple_mcp import FastMCP
from services.financial_service import FinHubService
from starlette.applications import Starlette
from starlette.routing import Route
from starlette.responses import JSONResponse

mcp = FastMCP("Financial Data Server")
financial_service = FinHubService()

@mcp.tool()
def get_stock_price(symbol: str) -> dict:
    """Fetches the live stock price and daily stats for a given stock symbol."""
    return financial_service.get_stock_price(symbol)

@mcp.tool()
def get_company_filings(symbol: str, limit: int = 5) -> list:
    """Retrieves the latest company SEC filings for a given stock symbol."""
    return financial_service.get_company_filings(symbol, limit)

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
    print("Starting Financial Data MCP Server on port 8001...")
    uvicorn.run(app, host="0.0.0.0", port=8001) 