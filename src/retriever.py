# Amaç: Proje klasöründeki .txt dosyalarını okuma ve sisteme tanıtma.
import os
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from src.config import OPENAI_API_KEY

# Proje kökünü bularak data klasör yollarını oluşturuyoruz
BASE_DIR   = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DOCS_DIR   = os.path.join(BASE_DIR, "data", "docs")
INDEX_PATH = os.path.join(BASE_DIR, "data", "faiss_index")


# data/docs altındaki tüm .txt’leri oku
# Metini belirlenen parçalrı ayır (chunk_size=1000, chunk_overlap=200)
# metni OpenAIEmbeddings ile embed et
# FAISS yapısına dönüştür ve yükle
def build_faiss_index(doc_dir: str = DOCS_DIR, index_path: str = INDEX_PATH):
    # Metin dosyalarını yükle
    loader = DirectoryLoader(doc_dir, glob="**/*.txt", loader_cls=TextLoader)
    docs = loader.load()

    # Metni parçalara böl
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = splitter.split_documents(docs)

    # Embedding
    embed = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)

    # Index yönetimi
    if os.path.exists(index_path):
        # Var olan index'i yükle
        faiss_index = FAISS.load_local(
            index_path, embed, allow_dangerous_deserialization=True
        )
    else:
        # Yani index oluştur ve kaydet
        faiss_index = FAISS.from_documents(chunks, embed)
        faiss_index.save_local(index_path)

    return faiss_index

# Indeksi hazırlar ve en benzer k parçayı getir
def get_retriever(k: int = 5):
    index = build_faiss_index()
    return index.as_retriever(search_kwargs={"k": k})