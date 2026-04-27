import csv

from lunr import lunr
import util

client = util.CLIENT

# Index the data from the CSV
with open("books.csv") as file:
    reader = csv.reader(file)
    rows = list(reader)
documents = [{"id": (i + 1), "body": " ".join(row)} for i, row in enumerate(rows[1:])]
index = lunr(ref="id", fields=["body"], documents=documents)

# Get the user question
user_question = "suggest me sme adventure books"

# Search the index for the user question
results = index.search(user_question)
matching_rows = [rows[int(result["ref"])] for result in results]

# Format as a markdown table, since language models understand markdown
matches_table = " | ".join(rows[0]) + "\n" + " | ".join(" --- " for _ in range(len(rows[0]))) + "\n"
matches_table += "\n".join(" | ".join(row) for row in matching_rows)

print("Found matches in csv:")
print(matches_table)

# Now we can use the matches to generate a response
SYSTEM_MESSAGE = """
You are a helpful assistant that answers questions about 
books based off a book data set available in books.csv.
It contains title, author, genre, language fields.
You must use the data set to answer the questions. 
You should not provide any information that is not in the provided in the sources.
"""

response = client.chat.completions.create(
    model=util.MODEL_NAME,
    temperature=0.3,
    messages=[
        {"role": "system", "content": SYSTEM_MESSAGE},
        {"role": "user", "content": f"{user_question}\nSources: {matches_table}"},
    ],
)

print(f"\nResponse : \n")
print(response.choices[0].message.content)