import os
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

# ================================
# CONFIG
# ================================

DB_PATH = "/app/Jurixai_db"

# ================================
# LOAD EMBEDDING MODEL
# ================================

print("\nLoading embedding model...\n")

embeddings = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)

# ================================
# CONNECT TO CHROMADB
# ================================

print("Connecting to JurixAI Database...\n")

db = Chroma(
    persist_directory=DB_PATH,
    embedding_function=embeddings
)

# ================================
# USER QUERY
# ================================

query = input("Enter your legal query: ")

print(f"\nUser Query: {query}\n")

# ================================
# SEARCH DATABASE
# ================================

print("Searching legal database...\n")

results = db.similarity_search_with_score(query, k=3)

# ================================
# PRINT RESULTS
# ================================

if not results:
    print("No relevant legal information found.")

else:
    for i, (doc, score) in enumerate(results):

        print("\n" + "=" * 70)
        print(f"MATCH {i+1}")
        print("=" * 70)

        # Metadata
        source = os.path.basename(
            doc.metadata.get("source", "Unknown Source")
        )

        page = doc.metadata.get("page", "Unknown Page")

        # Print Metadata
        print(f"\nSource PDF : {source}")
        print(f"Page Number: {page}")

        # Lower score = better match
        print(f"Relevance Score: {round(score, 4)}")

        # Print Content
        print("\nRetrieved Legal Text:\n")
        print(doc.page_content)

        print("\n" + "-" * 70)

print("\nQuery completed successfully.\n")
