from python.helpers.extension import Extension

class MemorySyncOnInit(Extension):
    """On init, note a shared memory channel key for cross-team comms."""
    async def execute(self, **kwargs):
        key = kwargs.get("channel","bug-bounty-collective")
        self.agent.short_term_memory.append(f"shared_channel={key}")
