from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings

DB_PATH = "vector_store"

def create_vector_store(text):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    docs = splitter.split_text(text)

    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/embedding-001"
    )

    db = FAISS.from_texts(
        docs,
        embeddings
    )

    db.save_local(DB_PATH)

def retrieve_context(query):

    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/embedding-001"
    )

    db = FAISS.load_local(
        DB_PATH,
        embeddings,
        allow_dangerous_deserialization=True
    )

    docs = db.similarity_search(
        query,
        k=3
    )

    return "\n".join(
        [doc.page_content for doc in docs]
    )