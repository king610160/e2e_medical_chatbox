from langchain_pinecone import PineconeVectorStore
from src.helper import load_pdf, text_split, download_hugging_face_embeddings

import os
from dotenv import load_dotenv
load_dotenv()
PINECONE_KEY = os.getenv('pinecone_key')
PINECONE_ENV = os.getenv('pinecone_env')

os.environ['PINECONE_INDEX_NAME'] = PINECONE_ENV
os.environ['PINECONE_API_KEY'] = PINECONE_KEY

extract_data = load_pdf('data/')
text_chunks = text_split(extract_data)
hug_embed = download_hugging_face_embeddings()
vectorstores = PineconeVectorStore(embedding=hug_embed)

vectorstores.from_documents(
    documents=text_chunks, 
    index_name=PINECONE_ENV,
    embedding=hug_embed
)