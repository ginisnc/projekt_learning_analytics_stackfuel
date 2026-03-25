from pdf_reader import read_pdf
from qg import InstructionQG


PDF_PATH = "data/sample.pdf"


def main():
    print("Reading PDF...")
    text = read_pdf(PDF_PATH)

    print("Generating question...")
    qg =InstructionQG()

    # limit input size for now
    snippet = text[:1000]

    print("\n--- RESULT ---\n")     
    print(snippet)

    question = qg.generate_question(snippet)

    print("\n--- RESULT ---\n")
    print(question)


if __name__ == "__main__":
    main()
