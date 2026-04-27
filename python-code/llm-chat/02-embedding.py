import util

client = util.CLIENT

text_input = "A quick brown fox jumps over the lazy dog."

embedding_response = client.embeddings.create(
    model = util.EMBEDDING_MODEL_NAME,
    dimensions= util.EMBEDDING_MODEL_DIMENSIONS,
    input = text_input,
)

embedding = embedding_response.data[0].embedding

print(embedding)
print(f"Dimensions:", len(embedding))

print(text_input)