import fitz  # PyMuPDF
import pytesseract
from PIL import Image
import camelot
import io

def extract_text(pdf_path):
    doc = fitz.open(pdf_path)
    pages = []
    for i, page in enumerate(doc):
        pages.append({
            "page": i + 1,
            "text": page.get_text()
        })
    return pages

def extract_tables(pdf_path):
    tables = camelot.read_pdf(pdf_path, pages="all")
    data = []
    for i, table in enumerate(tables):
        data.append({
            "table_id": i,
            "text": table.df.to_string()
        })
    return data

def extract_images_ocr(pdf_path):
    doc = fitz.open(pdf_path)
    images_text = []

    for page_index in range(len(doc)):
        page = doc[page_index]
        for img in page.get_images(full=True):
            xref = img[0]
            base = doc.extract_image(xref)
            image_bytes = base["image"]
            image = Image.open(io.BytesIO(image_bytes))
            text = pytesseract.image_to_string(image)

            images_text.append({
                "page": page_index + 1,
                "text": text
            })

    return images_text
