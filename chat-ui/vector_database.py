from langchain.document_loaders import DirectoryLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import SentenceTransformerEmbeddings
from langchain.vectorstores import Chroma


raw_documents = DirectoryLoader("../vietsov_crawler/embed_texts").load()
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
documents = text_splitter.split_documents(raw_documents)
#VoVanPhuc/sup-SimCSE-VietNamese-phobert-base
embedding = SentenceTransformerEmbeddings(model_name="paraphrase-MiniLM-L6-v2")
vectorDB = Chroma.from_documents(documents, embedding, collection_name="context")