# Amaç: Kullanıcı girişini alma ve kurgumuzdan geçirme
from src.llm_client import get_llm_client
from src.memory import get_history
from src.retriever import get_retriever
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

# LLM istemcisini al
_llm = get_llm_client()

# Her yeni kullanıcı girişinde
def chat(user_input: str, session_id: str = "default") -> str:
    # Human mesajını geçmişe ekle / Belleği al ve kullanıcı mesajını ekle
    history = get_history(session_id)
    history.messages.append(HumanMessage(content=user_input))

    # Retrieval - RAG / en alakalı k belge parçasını çek
    retriever = get_retriever(k=5)
    docs = retriever.invoke(user_input)
    context = "\n\n---\n\n".join([d.page_content for d in docs])

    # Bağlamı SYSTEM rolü mesajı olarak ekle
    history.messages.append(SystemMessage(content=f"Context:\n{context}"))

    # Modeli çağır / Tüm geçmişi modele gönder, yanıt al
    response = _llm.invoke(history.messages)

    # Sistemin cevabı, sadece metni döndür
    history.messages.append(AIMessage(content=response.content))
    return response.content

