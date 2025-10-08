from dotenv import load_dotenv
import os
import openai

# Load environment variables from a .env file
load_dotenv()

# Replace with your actual OpenAI API key
openai.base_url = "https://api.openai.com/v1"
openai.api_key = "YOUR_OPENAI_API_KEY"
openai.models = "gpt-4o"


# Example: Call the 'openai/github-copilot' model (if available to your account)
response = openai.chat.completions.create(
    # model="openai/github-copilot",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Write a Python function to add two numbers."}
    ]
)

print(response.choices[0].message.content)