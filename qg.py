import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

class GermanQAPipeline:
    def __init__(self):
        self.model_name = "google/flan-t5-small"
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(self.model_name)

    def get_chunks(self, text: str, chunk_size: int = 300):
        """Teilt den Text in handliche Wörter-Pakete auf."""
        words = text.split()
        return [" ".join(words[i : i + chunk_size]) for i in range(0, len(words), chunk_size)]

    def generate_qa(self, text: str):
        # Sicherstellen, dass 'text' verarbeitet wird
        chunks = self.get_chunks(text)
        results = []

        for i, chunk in enumerate(chunks):
            # Klarer, kurzer Prompt für flan-t5-small
            prompt = f"generate a question based on this text: {chunk}"
            
            inputs = self.tokenizer(prompt, return_tensors="pt", truncation=True, max_length=512)

            with torch.no_grad():
                outputs = self.model.generate(
                    **inputs, 
                    max_new_tokens=50,
                    num_beams=3,
                    early_stopping=True
                )

            question = self.tokenizer.decode(outputs[0], skip_special_tokens=True)

            # Wir speichern nur den Original-Context und die generierte Frage
            results.append({
                "chunk_id": i + 1,
                "context": chunk,
                "question": question
            })

        return results
