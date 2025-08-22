from python.helpers.tool import Tool, Response

class PromptExpand(Tool):
    """Expand a short prompt into a richer template with sections."""
    async def execute(self, **kwargs):
        idea = kwargs.get("idea","")
        template = f"""# Objective
{idea}

# Constraints
- Be concise
- Return JSON

# Output format
{{"result": "<text>", "notes": []}}
"""
        return Response(message=template, break_loop=False)
