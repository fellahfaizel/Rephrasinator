from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from src.rephraser import rephrase_with_tone
from src.grammar_corrector import correct_grammar

app = FastAPI(title="Intelligent Text Rephraser API")

# CORS for React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # later restrict to your frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TextRequest(BaseModel):
    text: str
    tone: str = "formal"

@app.post("/rephrase")
def rephrase_text(req: TextRequest):
    output = rephrase_with_tone(req.text, tone=req.tone)
    return {"rephrased": output}

@app.post("/grammar")
def grammar_check(req: TextRequest):
    corrected = correct_grammar(req.text)
    return {"corrected": corrected}

@app.post("/smart_rephrase")
def smart_rephrase(req: TextRequest):
    step1 = rephrase_with_tone(req.text, tone=req.tone)
    step2 = correct_grammar(step1)
    return {"final_output": step2}

@app.get("/")
def root():
    return {"message": "Rephrasinator backend is running!"}
