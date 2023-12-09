import os
from langchain.document_loaders import DirectoryLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import SentenceTransformerEmbeddings
from langchain.vectorstores import Chroma
from langchain.schema import Document
from pyvi.ViTokenizer import tokenize


# raw_documents = DirectoryLoader("../vietsov_crawler/embed_texts").load()
# text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
# documents = text_splitter.split_documents(raw_documents)
#paraphrase-MiniLM-L6-v2

directory = "../vietsov_crawler/embed_texts"
documents = []
for filename in os.listdir(directory):
    file_path = os.path.join(directory, filename)
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        documents.append(Document(page_content=tokenize(content.lower()), metadata={"source": file_path, "original_content": content}))

embedding = SentenceTransformerEmbeddings(model_name="VoVanPhuc/sup-SimCSE-VietNamese-phobert-base")
vectorDB = Chroma.from_documents(documents, embedding, collection_name="context")