from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("all-MiniLM-L6-v2")

tone_prompts = {
    "formal": "This sentence sounds professional and formal.",
    "informal": "This sentence sounds casual and conversational.",
    "friendly": "This sentence sounds warm and friendly.",
    "concise": "This sentence is short and to the point.",
    "creative": "This sentence sounds imaginative and expressive."
}

def tone_score(output_text, tone):
    if tone not in tone_prompts:
        return 0.0
    tone_emb = model.encode(tone_prompts[tone], convert_to_tensor=True)
    text_emb = model.encode(output_text, convert_to_tensor=True)
    return float(util.cos_sim(text_emb, tone_emb))
