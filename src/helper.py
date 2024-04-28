from langchain_community.embeddings import HuggingFaceEmbeddings

from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

def load_pdf(data):
    loader = DirectoryLoader(data,
                             glob='*.pdf',
                             loader_cls=PyPDFLoader)
    document = loader.load()
    return document


def text_split(data):
    text_spliter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=20)
    text_chunks = text_spliter.split_documents(data)

    return text_chunks

def download_hugging_face_embeddings():
    embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')
    return embeddings