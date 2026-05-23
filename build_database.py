import os
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

# Paths
LEGAL_DATA_PATH = "/app/legal_data"
DB_PATH = "/app/Jurixai_db"

# 1. Load PDFs
print("Loading all Legal PDFs from folder...")

loader = PyPDFDirectoryLoader(LEGAL_DATA_PATH)
pages = loader.load()

print(f"Total pages loaded: {len(pages)}")

# 2. Chunking
print("Splitting into chunks...")

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

chunks = text_splitter.split_documents(pages)

print(f"Total chunks created: {len(chunks)}")

# 3. Embeddings
print("Loading Embedding Model...")

embeddings = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)

# 4. Create ChromaDB
print("Creating Vector Database...")

db = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory=DB_PATH
)

print("Vector Database created successfully!")
