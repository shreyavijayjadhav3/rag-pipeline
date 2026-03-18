from langchain_huggingface import HuggingFaceEmbeddings

import os

os.environ["TOKENIZERS_PARALLELISM"] = "false"

model_name="BAAI/bge-small-en"
model_kwargs={"device":"cpu"}
encode_kwargs={"normalize_embeddings":True}

def create_embeddings():
    embeddings = HuggingFaceEmbeddings(
        model_name=model_name,
        model_kwargs=model_kwargs,
        encode_kwargs=encode_kwargs,
    )
    
    print("Embeddings created successfully")
    return embeddings