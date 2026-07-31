import os

class SarvamLLM:
    def __init__(self):
        self.api_key = os.getenv(
            "SARVAM_API_KEY"
        )
    def invoke(self, prompt):
        response = "Sarvam response"
        return response