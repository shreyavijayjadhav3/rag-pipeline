from langchain_community.vectorstores import FAISS
from create_embeddings import create_embeddings
from split_data import split_data

faiss_index="./vector_db/faiss_index"
def create_vector_db():
    documents = split_data()
    embeddings = create_embeddings()
    db = FAISS.from_documents(documents=documents,embedding=embeddings)
    db.save_local(faiss_index)
    print("Vector DB created successfully")

create_vector_db()