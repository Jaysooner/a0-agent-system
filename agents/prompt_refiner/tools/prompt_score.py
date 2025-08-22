from python.helpers.tool import Tool, Response

class PromptScore(Tool):
    """Score a prompt's clarity and testability on 0..100 with short tips."""
    async def execute(self, **kwargs):
        prompt = kwargs.get("prompt", "")
        score = 50
        tips = []
        if "steps" in prompt.lower(): score += 10
        if "constraints" in prompt.lower(): score += 10
        if "examples" in prompt.lower(): score += 10
        if len(prompt) > 300: score -= 10
        if "?" in prompt: tips.append("Convert open questions into directives where possible.")
        msg = f"score: {max(0,min(100,score))}\n" + "\n".join(f"- {t}" for t in tips)
        return Response(message=msg, break_loop=False)
