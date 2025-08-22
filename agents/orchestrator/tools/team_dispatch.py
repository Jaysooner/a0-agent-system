from python.helpers.tool import Tool, Response

class TeamDispatch(Tool):
    """Create a structured task card for another agent/team."""
    async def execute(self, **kwargs):
        task = kwargs.get("task","")
        assignee = kwargs.get("assignee","unknown")
        priority = kwargs.get("priority","P2")
        payload = {"assignee": assignee, "priority": priority, "task": task}
        return Response(message=str(payload), break_loop=False)
