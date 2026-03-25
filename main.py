from pdf_reader import read_pdf_dict
from qg import GermanQAPipeline


PDF_PATH = "data/sample.pdf"


def main():
    text = read_pdf_dict(PDF_PATH)

    qg = GermanQAPipeline()

    result = qg.generate_qa(text)

    print("\n--- RESULT ---\n")
    #print(text)

    print("QUESTION:", result)


if __name__ == "__main__":
    main()
