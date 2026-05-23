# JurixAI ⚖️  
## Empowering Legal Clarity with AI & Empathy

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![LangChain](https://img.shields.io/badge/LangChain-RAG-green)
![Docker](https://img.shields.io/badge/Docker-Containerized-blue)
![Kubernetes](https://img.shields.io/badge/Kubernetes-Orchestrated-326CE5)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

# 📌 Overview

JurixAI is an advanced AI-powered legal assistant designed specifically for the **Indian Legal System**.  
Built using **Retrieval-Augmented Generation (RAG)** architecture, JurixAI combines the power of **Large Language Models (LLMs)** with **trusted legal knowledge bases** to provide accurate, context-aware, and empathetic legal guidance.

Unlike generic AI chatbots, JurixAI is engineered to:

- Understand legal terminology
- Retrieve trusted legal context
- Reduce hallucinations
- Respond in a user-friendly way
- Support bilingual communication (English + Hinglish)

JurixAI acts like a **digital legal companion (“Legal Saathi”)** for common legal awareness and educational support.

---

# 🚀 Why JurixAI?

Millions of people struggle to understand:

- IPC Sections
- RTI Procedures
- POSH Guidelines
- FIR Filing Process
- Consumer Rights
- Cyber Crime Complaints
- Employment Laws
- Domestic Violence Laws

Legal information is often:
- Complicated
- Expensive to access
- Difficult to interpret
- Filled with technical jargon

JurixAI solves this by transforming complex legal information into:
✅ Simple explanations  
✅ Actionable guidance  
✅ Structured responses  
✅ Human-like empathetic conversations  

---

# 🎯 Core Objectives

- Make Indian legal information accessible
- Reduce fear around legal processes
- Provide instant legal educational assistance
- Simplify legal language for everyone
- Build AI systems with empathy-first interactions

---

# 🧠 Architecture Overview

```text
User Query
    │
    ▼
Embedding Generation
    │
    ▼
ChromaDB Vector Search
    │
    ▼
Relevant Legal Context Retrieval
    │
    ▼
Prompt Augmentation
    │
    ▼
Llama 3.3 (Groq Cloud)
    │
    ▼
Empathetic Legal Response
```

---

# 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| **Python 3.10+** | Backend Development |
| **LangChain** | RAG Orchestration |
| **Groq Cloud** | Ultra-fast LLM Inference |
| **Llama-3.3-70B-Versatile** | Large Language Model |
| **ChromaDB** | Vector Database |
| **HuggingFace Embeddings** | Semantic Embedding Generation |
| **Docker** | Application Containerization |
| **Docker Compose** | Multi-service Orchestration |
| **Kubernetes** | Production-grade Deployment |
| **ConfigMap** | Configuration Management |
| **Namespace** | Kubernetes Isolation |
| **GitHub Actions (Future)** | CI/CD Automation |

---

# 🔥 Key Features

## ⚖️ Legal Context Awareness
JurixAI uses legal documents as the primary source of truth instead of generating random internet-based answers.

---

## 🧠 Retrieval-Augmented Generation (RAG)
The system retrieves relevant legal chunks before generating responses, significantly reducing hallucinations.

---

## 🌐 Hinglish + English Support
Users can communicate naturally in:
- English
- Hinglish
- Mixed conversational language

---

## ❤️ Empathy-First Prompting
JurixAI is designed to:
- Calm stressed users
- Avoid robotic responses
- Communicate respectfully
- Provide supportive guidance

---

## 📚 Structured Legal Responses

Each response includes:
- Clear explanation
- Relevant legal sections
- Practical next steps
- Simplified language
- Action recommendations

---

## 🐳 Fully Dockerized
The application is containerized for:
- Easy deployment
- Environment consistency
- Scalability
- Portability

---

## ☸️ Kubernetes Native
Includes production-ready Kubernetes resources:
- Deployment
- Service
- ConfigMap
- Namespace

---

## 🔒 Environment-Based Secrets
Sensitive API keys are managed through:
- `.env`
- Kubernetes ConfigMap
- Future Secret Management Support

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
├── .env
│
├── data/
│   ├── IPC.pdf
│   ├── RTI.pdf
│   ├── POSH.pdf
│   └── Other Legal PDFs
│
├── Jurixai_db/
│
├── k8s/
│   ├── namespace.yaml
│   ├── deployment.yaml
│   ├── service.yaml
│   └── configmap.yaml
│
└── README.md
```

---

# ⚙️ Local Development Setup

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

### Linux / macOS

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

# 🔑 Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
MODEL_NAME=llama-3.3-70b-versatile
```

---

# 🧠 Build Vector Database

```bash
python build_database.py
```

This script:
- Loads legal PDFs
- Splits documents into chunks
- Generates embeddings
- Stores vectors inside ChromaDB

---

# 🚀 Run JurixAI

```bash
python chatbot.py
```

---

# 🐳 Docker Support

## Build Docker Image

```bash
docker build -t jurixai .
```

---

## Run Docker Container

```bash
docker run -p 8000:8000 jurixai
```

---

# 🐋 Docker Compose Support

## Start Application

```bash
docker-compose up --build
```

---

## Stop Application

```bash
docker-compose down
```

---

# ☸️ Kubernetes Deployment

JurixAI supports Kubernetes-based production deployment.

---

# 📦 Kubernetes Resources

| File | Purpose |
|---|---|
| `namespace.yaml` | Creates isolated namespace |
| `deployment.yaml` | Deploys application pods |
| `service.yaml` | Exposes application |
| `configmap.yaml` | Stores environment configuration |

---

# 🚀 Deploy on Kubernetes

## Step 1 — Create Namespace

```bash
kubectl apply -f k8s/namespace.yaml
```

---

## Step 2 — Apply ConfigMap

```bash
kubectl apply -f k8s/configmap.yaml
```

---

## Step 3 — Deploy Application

```bash
kubectl apply -f k8s/deployment.yaml
```

---

## Step 4 — Expose Service

```bash
kubectl apply -f k8s/service.yaml
```

---

# 🔍 Verify Deployment

## Check Pods

```bash
kubectl get pods -n jurixai
```

---

## Check Services

```bash
kubectl get svc -n jurixai
```

---

## Check Logs

```bash
kubectl logs <pod-name> -n jurixai
```

---

# 📈 Future Roadmap

## 🔮 Planned Features

- Voice-based legal assistant
- Regional Indian language support
- Fine-tuned Indian legal LLM
- WhatsApp integration
- Telegram Bot
- PDF legal report generation
- AI-powered FIR drafting
- Legal document summarization
- CI/CD pipelines
- Monitoring with Prometheus + Grafana
- Helm chart support

---

# 🔐 Security Considerations

JurixAI follows secure development practices:

- Environment variable protection
- Containerized deployments
- Kubernetes namespace isolation
- API key abstraction
- Reduced hallucination architecture using RAG

---

# 📚 Example Use Cases

## 👩‍⚖️ Legal Awareness
> “What should I do if my employer doesn't pay salary?”

---

## 🚨 Cyber Crime Guidance
> “How can I report online fraud in India?”

---

## 🏠 Consumer Rights
> “Can I return a defective product legally?”

---

## 👩 Women Safety & POSH
> “What protections exist under POSH Act?”

---

# ❤️ Empathy-Driven AI Experience

JurixAI is not just another chatbot.

It is designed to:
- Listen carefully
- Respond politely
- Guide responsibly
- Reduce panic during stressful legal situations

The AI intentionally avoids:
❌ Aggressive legal tone  
❌ Robotic responses  
❌ Overly technical explanations  

---

# ⚠️ Disclaimer

JurixAI is developed for:
- Educational purposes
- Research purposes
- Legal awareness

It is **NOT** a substitute for professional legal advice from a qualified advocate or lawyer.

Always verify legal information through:
- Official Government Sources
- Certified Legal Professionals

---

# 👨‍💻 Author

# Tushar Singh (backend developer)
# Nitin Panwar (Devops / Cloud intregation)

### Focus Areas
- Software Engineering
- Artificial Intelligence
- Machine Learning
- Backend Development
- DevOps & Cloud

---

# 🌐 GitHub

```bash
https://github.com/tusharsingh-sde
```

---

# 🤝 Contributing

Contributions are welcome!

## Contribution Flow

```bash
Fork Repository
    ↓
Clone Repository
    ↓
Create Feature Branch
    ↓
Commit Changes
    ↓
Push to GitHub
    ↓
Open Pull Request
```

---

# 📜 License

This project is licensed under the MIT License.

---

# ⭐ Support the Project

If you like this project:

⭐ Star the repository  
🍴 Fork the repository  
🛠️ Contribute improvements  
📢 Share with others  

---

# ⚖️ JurixAI — Your AI Legal Saathi ❤️
