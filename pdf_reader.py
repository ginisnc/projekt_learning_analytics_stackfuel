import fitz
import re

def read_pdf_dict(path: str) -> str:
    doc = fitz.open(path)
    paragraphs = []

    for page in doc:
        data = page.get_text("dict")
        
        # Sortiere Blöcke von oben nach unten, falls sie durcheinander gewürfelt sind
        blocks = sorted(data.get("blocks", []), key=lambda b: b["bbox"][1])

        for block in blocks:
            if block.get("type") != 0: # Überspringe Bilder/Grafiken
                continue

            lines = []
            for line in block.get("lines", []):
                spans = line.get("spans", [])
                line_text = "".join(span.get("text", "") for span in spans)
                lines.append(line_text)

            block_text = " ".join(lines) # Hier lieber direkt Leerzeichen statt \n

            # Cleaning
            block_text = re.sub(r"-\s+", "", block_text) # Silbentrennung am Zeilenende fixen
            block_text = re.sub(r"\s+", " ", block_text)
            block_text = block_text.strip()

            # Filter: Ignoriere sehr kurze Fragmente (z.B. Seitenzahlen, einzelne Wörter)
            # Ein Satz sollte meist mehr als 30 Zeichen haben, um sinnvoll zu sein.
            if len(block_text) > 40:
                paragraphs.append(block_text)

    doc.close() # Wichtig: Dokument wieder schließen
    return " ".join(paragraphs) # Ein sauberer, langer String für das Chunking
