"""
Simple MCP (Model Context Protocol) replacement
Since fast_mcp is not available, this provides basic MCP-like functionality
"""

class SimpleMCP:
    def __init__(self, name):
        self.name = name
        self.tools = {}
    
    def tool(self):
        """Decorator to register tools"""
        def decorator(func):
            self.tools[func.__name__] = {
                'function': func,
                'name': func.__name__,
                'description': func.__doc__ or f"Tool: {func.__name__}"
            }
            return func
        return decorator
    
    def get_tools(self):
        """Get all registered tools"""
        return self.tools
    
    def call_tool(self, tool_name, **kwargs):
        """Call a specific tool"""
        if tool_name in self.tools:
            return self.tools[tool_name]['function'](**kwargs)
        else:
            raise ValueError(f"Tool {tool_name} not found")

# Create a simple FastMCP alias for compatibility
FastMCP = SimpleMCP 