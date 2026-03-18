from langchain_text_splitters import RecursiveCharacterTextSplitter
from load_data import load_data

def split_data():
    documents = load_data()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=10)
    chunks = text_splitter.split_documents(documents=documents)
    print("Data split successfully")
    return chunks