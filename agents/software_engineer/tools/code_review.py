from python.helpers.tool import Tool, Response

class CodeReview(Tool):
    """Lightweight static review with simple heuristics and TODO list output."""
    async def execute(self, **kwargs):
        code = kwargs.get("code", "")
        findings = []
        if "print(" in code and "logging" not in code:
            findings.append("Consider using a structured logger instead of print().")
        if "TODO" in code:
            findings.append("Unresolved TODOs found.")
        msg = "\n".join(f"- {f}" for f in findings) or "No obvious issues found."
        return Response(message=msg, break_loop=False)
