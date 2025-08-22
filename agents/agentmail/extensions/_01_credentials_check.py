from python.helpers.extension import Extension

class CredentialsCheck(Extension):
    """On init, verify email credentials are configured; annotate state."""
    async def execute(self, **kwargs):
        ok = bool(self.agent.env.get("AGENTMAIL_API_KEY")) if hasattr(self.agent, "env") else False
        status = "agentmail_credentials=ok" if ok else "agentmail_credentials=missing"
        self.agent.short_term_memory.append(status)
