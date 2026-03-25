from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

class GermanQAPipeline:
    def __init__(self):
        model_name = "google/flan-t5-small"
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

    def generate_qa(self, text: str):

        prompt = f"""
Generate a question about the text that a teacher could ask.

Text:
{text}


Question:
"""

        inputs = self.tokenizer(prompt, return_tensors="pt", truncation=True)

        outputs = self.model.generate(
            **inputs,
            max_length=128,
            do_sample=True,
            temperature=0.7
        )

        question = self.tokenizer.decode(outputs[0], skip_special_tokens=True)

        return question
