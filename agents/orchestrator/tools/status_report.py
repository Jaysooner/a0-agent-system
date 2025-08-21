from python.helpers.tool import Tool, Response

class StatusReport(Tool):
    """Emit a concise status report skeleton."""
    async def execute(self, **kwargs):
        project = kwargs.get("project","General")
        sections = ["Summary","Completed","In-Progress","Risks","Next"]
        report = "\n".join([f"{project} :: {s}" for s in sections])
        return Response(message=report, break_loop=False)
