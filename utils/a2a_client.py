import httpx
import json

class A2AClient:
    """A simple client for interacting with A2A servers."""
    def __init__(self, remote_agent_url: str):
        self.url = remote_agent_url.rstrip('/') + '/'
        self.client = httpx.Client()

    def send_task(self, payload: dict) -> dict | None:
        """Sends a task to the remote agent and returns the final task object."""
        try:
            part = {"text": json.dumps(payload)}
            message = {"role": "user", "parts": [part]}
            request = {"message": message}
            
            response = self.client.post(self.url, json=request, timeout=120.0)
            response.raise_for_status()
            
            return response.json()
        except Exception as e:
            print(f"A2A task failed for {self.url}: {e}")
            return None 