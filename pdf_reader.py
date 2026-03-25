import fitz
import re


def read_pdf_dict(path: str) -> str:
    doc = fitz.open(path)
    paragraphs = []

    for page in doc:
        data = page.get_text("dict")

        for block in data.get("blocks", []): # type: ignore
            if block.get("type") != 0:
                continue

            lines = []

            for line in block.get("lines", []):
                spans = line.get("spans", [])
                line_text = "".join(span.get("text", "") for span in spans)
                lines.append(line_text)

            block_text = "\n".join(lines)

            # cleaning
            block_text = re.sub(r"-\n", "", block_text)
            block_text = block_text.replace("\n", " ")
            block_text = re.sub(r"\s+", " ", block_text)

            if block_text.strip():
                paragraphs.append(block_text.strip())

    return "\n\n".join(paragraphs)
