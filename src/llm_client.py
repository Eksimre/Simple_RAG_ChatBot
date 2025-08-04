# Amaç: Kullanacağımız LLM modelini yapılandıma
from src.config import OPENAI_API_KEY                # config.py’den API anahtarını al
from langchain_openai.chat_models import ChatOpenAI  # LLM modeli

def get_llm_client() -> ChatOpenAI:
    return ChatOpenAI(
        model_name="gpt-3.5-turbo",       # Kullanmak istediğiniz GPT modeli
        openai_api_key=OPENAI_API_KEY,    # API anahtarı
        temperature=0.0,                  # Deterministik oranı
    )