"""
Rephraser module: loads a seq2seq model and exposes rephrase() function.
Designed to work with Flan-T5 / T5 / BART models from Hugging Face.
"""

import os
from typing import List, Optional
import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

MODEL_NAME = os.environ.get("REPHRASINATOR_MODEL", "google/flan-t5-small")

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, use_fast = True)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)
model = model.to(DEVICE)
model.eval()

def build_prompt(text: str, style: Optional[str] = None) -> str:
    """
    Build a prompt for the seq2seq model.
    Keep it short and explicit. Example styles: 'formal', 'casual', 'concise'
    """
    if style:
        return f"Rephrase {style}: {text}"
    
    return f"Rephrase: {text}"

def generate_text(prompts, max_length=128, num_beams=4, temperature=1.0, do_sample=False):
    inputs = tokenizer(prompts, return_tensors="pt", padding=True, truncation=True)
    
    outputs = model.generate(
        **inputs,
        max_length=max_length,
        num_beams=num_beams,
        temperature=temperature,
        do_sample=do_sample
    )
    
    decoded = [tokenizer.decode(output, skip_special_tokens=True) for output in outputs]
    return decoded

def rephrase(text: str,
             style: Optional[str] = None,
             max_length: int = 128,
             num_beams: int = 4,
             temperature: float = 1.0,
             do_sample: bool = False) -> str:
    """
    High-level function: takes raw text and returns a single rephrased string.
    """
    prompt = build_prompt(text, style)
    outputs = generate_text([prompt], max_length=max_length, num_beams=num_beams, temperature=temperature, do_sample=do_sample)
    return outputs[0]

if __name__ == "__main__":
    # quick manual test when running the file
    examples = [
        "he dont has any idea about the topic.",
        "I can't attend the meeting tonight because i'm sick."
    ]
    for ex in examples:
        print("INPUT :", ex)
        print("OUTPUT:", rephrase(ex, style="formal"))
        print("-" * 50)