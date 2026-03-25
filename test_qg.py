from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

print("Loading model...")

model_name = "google/flan-t5-small"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

print("Model loaded.")

prompt = "Stelle eine Frage zum Thema: Garnelen leben im Meer."
inputs = tokenizer(prompt, return_tensors="pt")

print("Running generate...")

try:
    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_length=50
        )
    print("Generation finished.")
except Exception as e:
    print("ERROR DURING GENERATION:", e)
    raise

print("Decoding...")

result = tokenizer.decode(outputs[0], skip_special_tokens=True)

print("OUTPUT:")
print(result)
