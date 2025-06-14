from starlette.applications import Starlette
from starlette.routing import Route
from starlette.requests import Request
from fast_mcp.server.sse import SseServerTransport
from fast_mcp.server_v1 import Server

def create_starlette_app(mcp_server: Server, debug: bool = False) -> Starlette:
    """Creates a Starlette application that can serve the provided MCP server with SSE."""
    sse = SseServerTransport("/")

    async def handle_sse(request: Request) -> None:
        async with sse.connect_sse(
            request.scope, request.receive, request._send
        ) as (read_stream, write_stream):
            await mcp_server.run(
                read_stream, write_stream, mcp_server.create_initialization_options()
            )

    return Starlette(
        debug=debug,
        routes=[
            Route("/", endpoint=handle_sse, methods=["GET", "POST"]),
        ],
    ) 