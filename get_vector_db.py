from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from create_embeddings import create_embeddings

datafile="./vector_db/faiss_index"
def get_vector_db():
    embeddings = create_embeddings()
    db = FAISS.load_local(datafile,embeddings,allow_dangerous_deserialization = True)
    return db
    