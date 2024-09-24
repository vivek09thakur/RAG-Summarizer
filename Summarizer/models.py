import os
from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage
import load_dotenv from dotenv

token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.inference.ai.azure.com"
model_name = "Mistral-large"

client = MistralClient(api_key=token, endpoint=endpoint)

response = client.chat(
    model=model_name,
    messages=[
        ChatMessage(role="system", content="You are a helpful assistant."),
        ChatMessage(role="user", content="What is the capital of France?"),
    ],
    temperature=1.,
    max_tokens=1000,
    top_p=1.
)

print(response.choices[0].message.content)