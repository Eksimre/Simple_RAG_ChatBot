# Amaç: sohbet geçmişini Ram'de tutma ve sistem rolünü belirleme
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.messages import SystemMessage

# Session bazlı In-Memory sohbet geçmişlerini saklayacak sözlük
_history_store: dict[str, InMemoryChatMessageHistory] = {}

# session_id’ye göre bir InMemoryChatMessageHistory objesi dön
# yoksa oluştur en başta SYSTEM mesajını ekle
def get_history(session_id: str = "default") -> InMemoryChatMessageHistory:
    if session_id not in _history_store:
        history = InMemoryChatMessageHistory()
        # Sistem rolünü belirleme
        history.messages.append(
            SystemMessage(
                content=(
                    "Sen basit bir sanal asistansın. "
                    "Kullanıcının sorularını nazikçe, kısa ve öz şekilde yanıtla. "
                    "Tüm yanıtlarını Türkçe ver."
                )
            )
        )
        _history_store[session_id] = history
    return _history_store[session_id]