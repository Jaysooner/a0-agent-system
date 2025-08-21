from python.helpers.tool import Tool, Response

class InboxSearch(Tool):
    """Search mailbox by query and return a compact list."""
    async def execute(self, **kwargs):
        query = kwargs.get("query","")
        # Replace with real SDK call; here we stub results.
        results = [f"Match: {query} :: id=XYZ123"]
        return Response(message="\n".join(results), break_loop=False)
