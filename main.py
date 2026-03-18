from langchain_community.vectorstores import FAISS
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.retrieval import create_retrieval_chain
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from get_vector_db import get_vector_db
import os
from dotenv import load_dotenv

load_dotenv(override=True)
def get_answer(question):
    
    db = get_vector_db()
    
    llm = ChatGroq(model="llama3-8b-8192",api_key=os.environ["GROQ_API_KEY"])
    
    prompt = ChatPromptTemplate.from_template(
        """ 
        You are an assistant who will provide answers based on the provided document.
        if you do not find the answer, say I do not know the answer.
        context: {context}
        questions: {input}
        """
    )
    
    document_chain = create_stuff_documents_chain(llm=llm,prompt=prompt)
    
    retriever = db.as_retriever()
    
    retrieval_chain = create_retrieval_chain(retriever,document_chain)
    
    response = retrieval_chain.invoke({"input":question})
        
    return response["answer"]

answer = get_answer("Where is Shreya ?")

print(answer)