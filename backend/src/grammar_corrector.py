import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

MODEL_NAME = "vennify/t5-base-grammar-correction"
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME).to(DEVICE)
model.eval()

def correct_grammar(text: str, max_length: int = 128) -> str:
    prompt = "fix grammar: " + text
    inputs = tokenizer(prompt, return_tensors="pt", truncation=True).to(DEVICE)
    
    with torch.no_grad():
        outputs = model.generate(**inputs, max_length=max_length, num_beams=4, early_stopping=True)
    
    corrected = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return corrected

if __name__ == "__main__":
    test = "He dont has any idea about the topic."
    print("Before:", test)
    print("After :", correct_grammar(test))
