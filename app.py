from flask import Flask, render_template, jsonify, request
from src.helper import download_hugging_face_embeddings

from langchain_pinecone import PineconeVectorStore
from langchain.prompts import PromptTemplate
from langchain_community.llms import CTransformers
from langchain.chains import RetrievalQA
from dotenv import load_dotenv
from src.prompt import *
import os

app = Flask(__name__)

load_dotenv()
PINECONE_KEY = os.getenv('pinecone_key')
PINECONE_ENV = os.getenv('pinecone_env')

os.environ['PINECONE_INDEX_NAME'] = PINECONE_ENV
os.environ['PINECONE_API_KEY'] = PINECONE_KEY

# also need to embedding for embedding query
embedding = download_hugging_face_embeddings()

docsearch = PineconeVectorStore.from_existing_index(PINECONE_ENV, embedding)

PROMPT=PromptTemplate(template=prompt_template, input_variables=["context", "question"])
chain_type_kwargs={"prompt": PROMPT}

llm=CTransformers(model="model/llama-2-7b-chat.ggmlv3.q4_0.bin",
                  model_type="llama",
                  config={'max_new_tokens':512,
                          'temperature':0.8})

# retriever = docsearch.as_retriever(search_kwargs={'k': 2})

qa=RetrievalQA.from_chain_type(
    llm=llm, 
    chain_type="stuff", 
    retriever=docsearch.as_retriever(search_kwargs={'k': 2}),
    return_source_documents=True, 
    chain_type_kwargs=chain_type_kwargs)


@app.route('/')
def index():
    return render_template('chat.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)