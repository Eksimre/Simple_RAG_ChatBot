# Amaç: Testler için basit bir kod
from src.chatbot import chat

# Kullanıcı "exit" yazana kadar konuşma devam eder
# session_id=”default” ile tek bir geçmiş hattı kullanır
def main():
    print("=== ChatBot Project (Auto RAG+Chat) ===")
    print("Çıkmak için 'exit' yazın.\n")

    while True:
        user_input = input("Siz: ").strip()
        if user_input.lower() == "exit":
            print("Bot: Görüşmek üzere!")
            break
        reply = chat(user_input, session_id="default")
        print(f"Bot: {reply}\n")

if __name__ == "__main__":
    main()