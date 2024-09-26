from dotenv import load_dotenv
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage,UserMessage
from azure.core.credentials import AzureKeyCredential
import os

class MODEL_GENERATOR:
    def __init__(self,token,endpoint,model_name) -> None:
        self.token = token
        self.endpoint = endpoint
        self.model_name = model_name
        self.client = ChatCompletionsClient(
            endpoint=self.endpoint,
            credential=AzureKeyCredential(self.token)
        )
        pass
    
    def complete(self,prompt):
        completion = self.client.complete(
            messages=[
                SystemMessage(
                    content='''
                    Your name is XDEA. An AI which is capable of thinking and reasoning for long context 
                    '''
                )
            ]
        )