from python.helpers.extension import Extension

class AutoFeedbackLoop(Extension):
    """Attach a tiny rubric to the agent name for downstream evaluators."""
    async def execute(self, **kwargs):
        rubric = "Rubric: clear objective • constraints • eval check"
        self.agent.agent_name = f"{self.agent.agent_name} [{rubric}]"
