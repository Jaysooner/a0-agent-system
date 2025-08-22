from python.helpers.extension import Extension

class GitContextLoader(Extension):
    """On agent init, annotate memory with current git branch if available."""
    async def execute(self, **kwargs):
        try:
            import subprocess
            branch = subprocess.check_output(["git","rev-parse","--abbrev-ref","HEAD"], text=True).strip()
            self.agent.short_term_memory.append(f"git_branch={branch}")
        except Exception:
            pass
