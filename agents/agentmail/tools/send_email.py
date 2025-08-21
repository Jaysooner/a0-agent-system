from python.helpers.tool import Tool, Response

class SendEmail(Tool):
    """Draft and send an email (stubbed)."""
    async def execute(self, **kwargs):
        to = kwargs.get("to","")
        subject = kwargs.get("subject","")
        body = kwargs.get("body","")
        preview = f"TO: {to}\nSUBJECT: {subject}\n\n{body}"
        return Response(message=f"[DRY-RUN]\n{preview}", break_loop=False)
