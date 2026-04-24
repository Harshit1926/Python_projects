import fitz  # PyMuPDF
import pytesseract
from PIL import Image
from langchain_text_splitters import RecursiveCharacterTextSplitter
import os

# Windows only — point to your tesseract install path
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def load_pdf(pdf_path: str) -> str:
    """Extract text from a PDF — handles both digital and scanned PDFs."""
    doc = fitz.open(pdf_path)
    full_text = ""

    for page_num, page in enumerate(doc):
        # first try normal text extraction
        text = page.get_text().strip()

        """If a PDF page doesn’t have selectable text, it’s probably just an image — so use OCR to read it."""
        if not text:
            print(f"Page {page_num + 1} has no text — running OCR...")
            pix = page.get_pixmap(dpi=300)  # render page as image
            img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
            text = pytesseract.image_to_string(img)

        full_text += f"\n[Page {page_num + 1}]\n{text}\n"

    doc.close()
    return full_text


def load_image(image_path: str) -> str:
    """Extract text from a plain image file using OCR."""
    print(f"Running OCR on image: {image_path}")
    img = Image.open(image_path)
    text = pytesseract.image_to_string(img)
    return f"\n[Image: {os.path.basename(image_path)}]\n{text}\n"


def load_file(file_path: str) -> str:
    """Auto-detect file type and extract text accordingly."""
    ext = os.path.splitext(file_path)[1].lower()

    if ext == ".pdf":
        return load_pdf(file_path)
    elif ext in [".jpg", ".jpeg", ".png", ".bmp", ".tiff"]:
        return load_image(file_path)
    elif ext == ".txt":
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    else:
        raise ValueError(f"Unsupported file type: {ext}")


def chunk_text(text: str, chunk_size=500, chunk_overlap=50):
    """Split text into overlapping chunks."""
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=["\n\n", "\n", ".", " "]
    )
    return splitter.split_text(text)


def process_file(file_path: str):
    """Full pipeline: any file → text → chunks."""
    print(f"Loading: {file_path}")
    text = load_file(file_path)
    print(f"Extracted {len(text)} characters")

    chunks = chunk_text(text)
    print(f"Created {len(chunks)} chunks\n")
    return chunks


if __name__ == "__main__":
    # test with a PDF
    path = "data/sample.pdf"
    if os.path.exists(path):
        chunks = process_file(path)
        for i, chunk in enumerate(chunks[:3]):
            print(f"--- Chunk {i+1} ---")
            print(chunk[:200])
            print()
    else:
        print("Add a file to data/ folder first!")