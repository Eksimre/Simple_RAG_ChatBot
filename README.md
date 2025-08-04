# LLM, LongChain & RAG ChatBot Projesi

## Açıklama
Bu proje, Python tabanlı bir chatbot uygulamasıdır ve modern **LLM (Large Language Model)** yaklaşımlarını kullanır.
LongChain, **Retrieval-Augmented Generation (RAG)** ve **OpenAI API** entegrasyonuyla, hem dil modeli tabanlı hem de doküman tabanlı bilgi sorgulama imkânı sunar.

## Özellikler

- **LLM**: OpenAI gibi büyük dil modelleri ile doğal dil işleme ve metin üretimi.
- **RAG**: Projedeki `data/docs` klasörü altındaki dokümanlardan yararlanarak daha doğru ve güncel yanıtlar.
- **LangChain / LongChain**: LLM süreçlerini zincirleme (chain) mantığıyla birbirine bağlayarak esnek ve ölçeklenebilir iş akışları.
- **Memory**: Kullanıcı geçmişini saklayarak bağlamsal sohbet imkânı.
- **FastAPI**: İstenirse hızlı ve kolay entegrasyon.

## Dosya Yapısı
- ChatBot_Project/
- ├── .gitignore           # Versiyon kontrolünde hariç tutulan dosyalar
- ├── README.md            # Proje tanıtım dosyası
- ├── requirements.txt     # Proje bağımlılık listesi
- ├── data/
- │   ├── docs/            # Sorgulama için kullanılacak dokümanlar
- │   └── faiss_index/     # RAG için oluşturulan vektör index
- ├── src/                 # Uygulama kaynak kodları
- │   ├── chatbot.py       # Ana chatbot iş mantığı
- │   ├── config.py        # Ortam değişkenleri ve ayarlar
- │   ├── llm_client.py    # LLM API istemcisi
- │   ├── main.py          # FastAPI sunucu başlangıç noktası
- │   ├── memory.py        # Konuşma geçmişi yönetimi
- │   └── retriever.py     # Doküman tabanlı bilgi çekme (RAG)
- └── .venv/               # Sanal ortam klasörü (ignore edilir)
