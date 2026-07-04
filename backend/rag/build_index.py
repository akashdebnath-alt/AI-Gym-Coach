from backend.rag.vectorstore import create_vectorstore

if __name__ == "__main__":

    print("=" * 50)
    print("Building FAISS Knowledge Base...")
    print("=" * 50)

    create_vectorstore()

    print()
    print("Knowledge Base Created Successfully!")
    print("=" * 50)