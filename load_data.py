from langchain_community.document_loaders.text import TextLoader

file_path="./source/INTRODUCTION.txt"

def load_data():
    text_loader = TextLoader(file_path=file_path,encoding="utf-8")
    documents = text_loader.load()
    print("Data loaded successfully")
    return documents