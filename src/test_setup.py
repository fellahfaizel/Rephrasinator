import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# AutoTokenizer is a 
# AutoModelForSeq2SeqLM is a 

print("Torch version: ",torch.__version__)

model_name = "google/flan-t5-small"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

input_text = "rephrase: he dont has any idea."
inputs = tokenizer(input_text, return_tensors="pt")
outputs = model.generate(**inputs, max_length=50)
print("Output: ", tokenizer.decode(outputs[0], skip_special_tokens=True))