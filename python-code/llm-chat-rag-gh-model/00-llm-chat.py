import util

client = util.CLIENT

query = "Which model are you?"

response = client.chat.completions.create(
    model=util.MODEL_NAME,
    messages = [
        # {"role": "system", "content":"You are a helpful, funny, dheerful agent. Respond with respect and clarity."},
        {"role": "user", "content": query}
    ],
)

print("Response:")

print(response.choices[0].message.content)
