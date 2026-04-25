API_KEY = "{API_KEY}"
BASE_URL="{Model_URL}"
MODEL_DEPLOYMENT_NAME="{Model_Deployment_Name}" 

from agent_framework.openai import OpenAIChatClient

client = OpenAIChatClient(
    base_url=BASE_URL,
    api_key=API_KEY,
    model=MODEL_DEPLOYMENT_NAME,
)