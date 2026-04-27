from langchain_community.document_loaders import TextLoader
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import Chroma
from langchain_text_splitters import CharacterTextSplitter
from langchain_classic.chains import RetrievalQA
import util
# 1 - Load and Chunk

loader = TextLoader("books.csv")

documents = loader.load()

text_splitter = CharacterTextSplitter(chunk_size = 1000, chunk_overlap = 0)
texts = text_splitter.split_documents(documents)

# 2 - Embedding 
embeddings = OpenAIEmbeddings(
    base_url= util.BASE_URL,
    api_key = util.API_KEY,
    model = util.EMBEDDING_MODEL_NAME,
    dimensions = util.EMBEDDING_MODEL_DIMENSIONS,
)

db = Chroma.from_documents(texts)

# 3 - LLM to retrieve 
qa_chain = RetrievalQA.from_chain_type(
    llm = ChatOpenAI(
        model=util.MODEL_NAME, 
        api_key= util.API_KEY, 
        base_url= util.BASE_URL,
    ),

    chain_type = "stuff", 
    retriever = db.as_retriever(),
)

response = qa_chain.invoke("What does the document say about Adventure?")
print(response["result"])
