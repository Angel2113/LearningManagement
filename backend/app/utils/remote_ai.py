import boto3
import json

class AIClient:

    def __init__(self):
        self.bedrock_runtime = boto3.client(
            service_name='bedrock-runtime',
            region_name='us-east-1'
        )
        self.model_id = "amazon.nova-lite-v1:0"
        self.messages = {
            "role": "user",
            "content": []
        }

    def chat(self, message):
        body = json.dumps({
                "messages": [
                    {
                        "role": "user",
                        "content": [
                            {"text": message
                            }
                        ]
                    }
                ],
                "inferenceConfig": {
                    "maxTokens": 200,
                    "temperature": 0.7,
                    "topP": 0.9
                }
            })
        response = self.bedrock_runtime.invoke_model(
            body=body,
            modelId=self.model_id,
            accept="application/json",
            contentType="application/json"
        )
        response_body = json.loads(response["body"].read())
        return response_body["output"]["message"]["content"][0]["text"]
