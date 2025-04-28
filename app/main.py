from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("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")

app = FastAPI()

# Allow CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "MailGenie AI Backend is running"}

@app.post("/chat/")
async def chat_with_ai(prompt: str):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # or gpt-4
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        return {"reply": response['choices'][0]['message']['content']}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
