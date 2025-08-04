# Amaç: .env dosyasında bulunan değişkenleri okumak ve doğrulamak.
import os
from dotenv import load_dotenv

# .env dosyasını oku ve ortam değişkenlerine aktar
load_dotenv()

# OpenAI API anahtarını al; yoksa hata ver
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise RuntimeError("OPENAI_API_KEY eksik – .env dosyasını güncelleyin.")

# LangChain API anahtarını al, yoksa hata ver
LANGCHAIN_API_KEY = os.getenv("LANGCHAIN_API_KEY")
if not LANGCHAIN_API_KEY:
    raise RuntimeError("LANGCHAIN_API_KEY eksik – .env dosyasını güncelleyin.")

# LangChain kütüphanelerinin de bu anahtarı okumasını sağla
os.environ["LANGCHAIN_API_KEY"] = LANGCHAIN_API_KEY

