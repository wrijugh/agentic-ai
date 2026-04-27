# Using free GitHub Model
import openai

BASE_URL="https://models.github.ai/inference"
API_KEY="{GitHub Token}"

CLIENT = openai.OpenAI(
    base_url=BASE_URL, 
    api_key=API_KEY)

MODEL_NAME = "openai/gpt-4o"

EMBEDDING_MODEL_NAME="openai/text-embedding-3-small"
EMBEDDING_MODEL_DIMENSIONS = 1536