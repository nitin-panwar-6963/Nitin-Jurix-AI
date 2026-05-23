import os
import io
import random
import pdfplumber
import pytesseract

from dotenv import load_dotenv
from PIL import Image

from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
from langchain_chroma import Chroma

# =========================================================
# ENVIRONMENT SETUP
# =========================================================

load_dotenv()

os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

# =========================================================
# TESSERACT SETUP
# =========================================================

pytesseract.pytesseract.tesseract_cmd = "/usr/bin/tesseract"

# =========================================================
# FASTAPI APP
# =========================================================

app = FastAPI(
    title="Jurix Vakeel Saab ⚖️",
    description="Friendly Indian Legal AI Assistant"
)

# =========================================================
# CORS
# =========================================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# =========================================================
# LOAD VECTOR DB + AI
# =========================================================

print("⚖️ Loading Jurix Vakeel Saab...")

DB_PATH = "./Jurixai_db"

embeddings = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)

db = Chroma(
    persist_directory=DB_PATH,
    embedding_function=embeddings
)

llm = ChatGroq(
    model_name="llama-3.3-70b-versatile",
    temperature=0.6
)

print("✅ Jurix Vakeel Saab Ready!")

# =========================================================
# CHAT MEMORY
# =========================================================

chat_memory = {}

# =========================================================
# POLITE GREETINGS
# =========================================================

greetings = [
    "👋 Hello ji! Welcome to Jurix Vakeel Saab ⚖️\nKaise help kar sakta hoon aapki aaj? 😊",

    "⚖️ Namaste ji! Jurix Vakeel Saab mein aapka warmly welcome hai 😊\nAap apna legal question ya problem share kar sakte hain.",

    "😊 Hello dost! Main Jurix Vakeel Saab hoon ⚖️\nTension free hokar apni problem batayiye, main best possible legal guidance dene ki puri koshish karunga.",

    "👨‍⚖️ Welcome ji!\nAap befikr hokar apna sawaal pooch sakte hain 😊",

    "🙏 Namaste! JurixAI mein aapka swagat hai ⚖️\nMain simple aur practical legal help provide karne ke liye yahan hoon."
]

# =========================================================
# REQUEST MODEL
# =========================================================

class UserRequest(BaseModel):
    session_id: str
    message: str

# =========================================================
# HOME ROUTE
# =========================================================

@app.get("/")
async def home():

    return {
        "status": "running",
        "message": "⚖️ Jurix Vakeel Saab Backend Running Successfully 🚀"
    }

# =========================================================
# HEALTH CHECK
# =========================================================

@app.get("/health")
async def health():

    try:

        response = llm.invoke("Hello")

        return {
            "status": "healthy",
            "llm_connected": True,
            "sample_response": response.content
        }

    except Exception as e:

        return {
            "status": "error",
            "message": str(e)
        }

# =========================================================
# FILE UPLOAD API
# =========================================================

@app.post("/upload")
async def process_document(file: UploadFile = File(...)):

    try:

        content = await file.read()

        extracted_text = ""

        # PDF PROCESSING

        if file.filename.lower().endswith(".pdf"):

            with pdfplumber.open(io.BytesIO(content)) as pdf:

                for page in pdf.pages:

                    text = page.extract_text()

                    if text:
                        extracted_text += text + "\n"

        # IMAGE OCR

        elif file.filename.lower().endswith((".png", ".jpg", ".jpeg")):

            image = Image.open(io.BytesIO(content))

            extracted_text = pytesseract.image_to_string(image)

        else:

            raise HTTPException(
                status_code=400,
                detail="❌ Sirf PDF, JPG, PNG, JPEG files allowed hain."
            )

        cleaned_text = " ".join(extracted_text.split())

        return {
            "status": "success",
            "filename": file.filename,
            "extracted_text": cleaned_text
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=f"❌ File processing mein error aa gaya: {str(e)}"
        )

# =========================================================
# MAIN CHAT API
# =========================================================

@app.post("/chat")
async def chat_with_jurix(request: UserRequest):

    session_id = request.session_id
    user_msg = request.message.strip()

    # =====================================================
    # CREATE SESSION
    # =====================================================

    if session_id not in chat_memory:
        chat_memory[session_id] = []

    # =====================================================
    # CHAT HISTORY
    # =====================================================

    history = chat_memory[session_id][-4:]

    history_text = "\n".join([
        f"{msg['role']}: {msg['text']}"
        for msg in history
    ])

    # =====================================================
    # VECTOR SEARCH
    # =====================================================

    results = db.similarity_search(user_msg, k=5)

    context_text = "\n\n".join([
        doc.page_content
        for doc in results
    ])

    # =====================================================
    # EMOTIONAL DETECTION
    # =====================================================

    emotional_keywords = [
        "fraud",
        "scam",
        "harassment",
        "abuse",
        "threat",
        "urgent",
        "help",
        "police",
        "crime",
        "cyber crime",
        "fear",
        "panic",
        "violence",
        "cheated",
        "domestic violence",
        "mental harassment"
    ]

    is_emotional = any(
        word in user_msg.lower()
        for word in emotional_keywords
    )

    emotional_state = (
        "Distressed User"
        if is_emotional
        else "Normal User"
    )

    # =====================================================
    # RANDOM GREETING
    # =====================================================

    random_greeting = random.choice(greetings)

    # =====================================================
    # MAIN PROMPT
    # =====================================================

    prompt = f"""
You are Jurix Vakeel Saab ⚖️ — an advanced Indian Legal AI Assistant.

Your personality should feel:
- Warm
- Respectful
- Polite
- Intelligent
- Practical
- Human-like
- Calm and supportive

━━━━━━━━━━━━━━━━━━━━━━━
💬 CONVERSATION STYLE RULES:

- Always greet politely and naturally.
- Make the user feel comfortable and welcome.
- Use natural Hinglish mixed with English.
- Speak like a smart helpful legal advisor.
- Use emojis softly and professionally 😊⚖️
- Never sound robotic.
- Never repeat same greeting every time.
- Keep tone respectful and friendly.
━━━━━━━━━━━━━━━━━━━━━━━

━━━━━━━━━━━━━━━━━━━━━━━
🧠 RESPONSE INTELLIGENCE RULES:

- If the user is stressed → be supportive.
- If the user asks normal legal questions → answer directly and smartly.
- Give practical and actionable solutions.
- Keep explanations simple.
- Use bullet points for clarity.
- Explain legal sections in easy language.
- Give best immediate action first.
━━━━━━━━━━━━━━━━━━━━━━━

━━━━━━━━━━━━━━━━━━━━━━━
⚖️ LEGAL RULES:

- Stay strictly within Indian law.
- Never create fake legal sections.
- Give realistic legal guidance only.
- Mention laws and sections if available.
━━━━━━━━━━━━━━━━━━━━━━━

━━━━━━━━━━━━━━━━━━━━━━━
🎯 RESPONSE QUALITY RULES:

- Avoid robotic formatting.
- Keep responses clean and readable.
- Use spacing properly.
- Avoid very long paragraphs.
- Sound natural and conversational.
━━━━━━━━━━━━━━━━━━━━━━━

Greeting to use:
{random_greeting}

User Emotional State:
{emotional_state}

━━━━━━━━━━━━━━━━━━━━━━━
PAST CONVERSATION:
{history_text}

━━━━━━━━━━━━━━━━━━━━━━━
LEGAL CONTEXT:
{context_text}

━━━━━━━━━━━━━━━━━━━━━━━
USER MESSAGE:
{user_msg}
"""

    # =====================================================
    # LLM RESPONSE
    # =====================================================

    response = llm.invoke(prompt)

    final_reply = response.content

    # =====================================================
    # SAVE MEMORY
    # =====================================================

    chat_memory[session_id].append({
        "role": "User",
        "text": user_msg
    })

    chat_memory[session_id].append({
        "role": "JurixAI",
        "text": final_reply
    })

    # =====================================================
    # RETURN RESPONSE
    # =====================================================

    return {
        "reply": final_reply
    }
