from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader

KNOWLEDGE_PATH = "knowledge"


def load_documents():

    documents = []

    pdf_files = Path(KNOWLEDGE_PATH).glob("*.pdf")

    for pdf in pdf_files:

        print(f"Loaded: {pdf.name}")

        loader = PyPDFLoader(str(pdf))

        documents.extend(loader.load())

    return documents