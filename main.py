import json
import os

from pdf_reader import read_pdf_dict
from qg import GermanQAPipeline

PDF_PATH = "data/sample.pdf"
OUTPUT_PATH = "data/questions.json"


def save_results_to_json(data, filename):
    """Speichert die Liste der Fragen und Kontexte sauber in eine Datei."""
    # Erstelle den Ordner, falls er nicht existiert
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print(f"\n[Success] Results saved to {filename}")


def main():
    print("Reading PDF...")
    text = read_pdf_dict(PDF_PATH)

    print("Initializing Model...")
    qg = GermanQAPipeline()

    results = qg.generate_qa(text)

    print("\n--- GENERATED QUESTIONS ---")
    output_data = []

    for i, item in enumerate(results):
        print(f"Q{i + 1}: {item['question']}")
        output_data.append(
            {"id": i + 1, "context": item["context"], "question": item["question"]}
        )

    # Speichern
    save_results_to_json(output_data, OUTPUT_PATH)

if __name__ == "__main__":
    main()
