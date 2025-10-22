from ollama import Client

OLLAMA_URL = "http://192.168.0.28:11434"

class AIClient:

    def __init__(self, model="None"):
        self.model = model
        self.messages = []
        self.client = Client(host=OLLAMA_URL)

    def chat(self, message):
        self.messages.append(
            {
                "role": "user",
                "content": message
            }
        )
        response = self.client.chat(self.model, messages=self.messages)

        self.messages.append(
            {
                "role": "assistant",
                "content": response['message']['content']
            }
        )
        return response['message']['content']

