from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

class InstructionQG:
    def __init__(self, model_name="bigscience/mt0-base"):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

    def generate_question(self, text):
        prompt = f"""
        Du bist ein Lehrer.

        Lies den folgenden Text und erstelle eine inhaltlich sinnvolle Frage,
        die das Verständnis prüft (keine reine Wiedergabe).

        Text:
        {text}

        Frage auf Deutsch:
        """

        inputs = self.tokenizer(
            prompt,
            return_tensors="pt",
            truncation=True,
            max_length=512
        )

        outputs = self.model.generate(
            **inputs,
            max_length=64,
            num_beams=4,
            temperature=0.7
        )

        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)
