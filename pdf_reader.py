import fitz  


def read_pdf(path: str) -> str:
    doc = fitz.open(path)
    text = ""

    for page in doc:
        text = text + str(page.get_text())

    # basic cleanup
    text = text.encode("utf-8", errors="ignore").decode()

    return text
