# JurixAI ⚖️  
### Empowering Legal Clarity with AI & Empathy

JurixAI is a high-performance, RAG-based (Retrieval-Augmented Generation) legal assistant built specifically for the Indian Legal System.  
It acts as a smart **“Legal Saathi”** that simplifies complex legal information while maintaining an empathetic, human-centric conversational experience.

---

# 🚀 What Problem Does JurixAI Solve?

Indian laws can be overwhelming due to:

- Complex legal terminology
- Lengthy legal documents
- Lack of accessible legal guidance
- Delayed legal assistance

JurixAI bridges this gap by:

✅ Simplifying legal sections like IPC, RTI, POSH, etc.  
✅ Providing instant, actionable legal guidance  
✅ Responding in natural Hinglish/English  
✅ Maintaining empathy while answering sensitive legal concerns  

---

# 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| **Llama-3.3-70B-Versatile** | Fast AI inference via Groq Cloud |
| **LangChain** | RAG orchestration pipeline |
| **ChromaDB** | Vector database for legal embeddings |
| **HuggingFace Embeddings** | Semantic search using all-MiniLM-L6-v2 |
| **Python 3.10+** | Backend environment |
| **Docker** | Containerization |
| **Docker Compose** | Multi-container orchestration |
| **Kubernetes** | Production deployment |
| **ConfigMap** | Environment configuration |
| **Namespace** | Kubernetes isolation |

---

# 🧠 How JurixAI Works (RAG Pipeline)

## 1️⃣ Data Ingestion
Indian law PDFs are loaded and divided into semantic chunks.

## 2️⃣ Vectorization
Chunks are converted into embeddings and stored inside `Jurixai_db`.

## 3️⃣ Retrieval
When a user asks a question, JurixAI retrieves the **Top 8 relevant legal contexts**.

## 4️⃣ Augmentation
Retrieved context is passed to Llama 3.3 using a custom **Empathy-First Prompt**.

## 5️⃣ Generation
JurixAI generates a structured, simplified response in:
- English
- Hinglish

---

# 🛡️ Key Features

## ⚖️ Context-Aware Legal AI
JurixAI answers only from trusted legal documents and minimizes hallucinations.

## 🌐 Bilingual Support
Supports:
- English
- Hinglish

## 🧾 Structured Responses
Provides:
- “The #1 Ultimate Action”
- Relevant legal sections
- Practical next steps

## ❤️ Empathy-First Communication
Designed to support users calmly during stressful legal situations.

## 🐳 Dockerized Deployment
Fully containerized for portability and scalability.

## ☸️ Kubernetes Ready
Production-ready Kubernetes manifests included:
- Deployment
- Service
- ConfigMap
- Namespace

---

# 📂 Project Structure

```bash
JurixAI/
│
├── chatbot.py
├── build_database.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
│
├── k8s/
│   ├── namespace.yaml
│   ├── deployment.yaml
│   ├── service.yaml
│   └── configmap.yaml
│
├── data/
├── Jurixai_db/
└── README.md
```

---

# ⚙️ Installation & Setup

## 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/JurixAI.git
cd JurixAI
```

---

## 2️⃣ Create Virtual Environment

### Windows

```bash
python -m venv .venv
.\.venv\Scripts\activate
```

### Linux/Mac

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Configure Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_api_key_here
```

---

## 5️⃣ Initialize Vector Database

```bash
python build_database.py
```

---

## 6️⃣ Run JurixAI

```bash
python chatbot.py
```

---

# 🐳 Docker Setup

## Build Docker Image

```bash
docker build -t jurixai .
```

## Run Container

```bash
docker run -p 8000:8000 jurixai
```

---

# 🐋 Docker Compose Setup

## Start Services

```bash
docker-compose up --build
```

## Stop Services

```bash
docker-compose down
```

---

# ☸️ Kubernetes Deployment

## Apply Namespace

```bash
kubectl apply -f k8s/namespace.yaml
```

## Apply ConfigMap

```bash
kubectl apply -f k8s/configmap.yaml
```

## Deploy Application

```bash
kubectl apply -f k8s/deployment.yaml
```

## Expose Service

```bash
kubectl apply -f k8s/service.yaml
```

---

# 📦 Kubernetes Resources Included

| Resource | Purpose |
|---|---|
| `namespace.yaml` | Creates isolated namespace |
| `deployment.yaml` | Deploys JurixAI pods |
| `service.yaml` | Exposes application |
| `configmap.yaml` | Stores environment configs |

---

# 🔍 Verify Kubernetes Deployment

## Check Pods

```bash
kubectl get pods -n jurixai
```

## Check Services

```bash
kubectl get svc -n jurixai
```

## View Logs

```bash
kubectl logs <pod-name> -n jurixai
```

---

# 🛡️ Disclaimer

JurixAI is developed for:

- Educational purposes
- Research purposes

It is **NOT** a replacement for professional legal advice.  
Always consult a qualified lawyer and verify legal information through official government resources.

---

# 👨‍💻 Author

## Tushar Singh

### Focus Areas
- Software Engineering
- AI/ML
- Software Development
- DevOps

### GitHub

```bash
https://github.com/tusharsingh-sde
```

---

# ⭐ Future Improvements

- Voice-based legal assistant
- Multi-language Indian support
- Legal document summarization
- Fine-tuned Indian legal LLM
- WhatsApp/Telegram integration
- Cloud-native deployment pipeline

---

# 🤝 Contributing

Contributions are welcome!

```bash
Fork → Clone → Create Branch → Commit → Push → Pull Request
```

---

# 📜 License

This project is licensed under the MIT License.

---

## ⚖️ JurixAI — “Your AI Legal Saathi” ❤️
