import PyPDF2
import docx

def extract_text_from_pdf(file):
    text = ""
    pdf_reader = PyPDF2.PdfReader(file.file)

    for page in pdf_reader.pages:
        text += page.extract_text() or ""

    return text


def extract_text_from_docx(file):
    text = ""
    doc = docx.Document(file.file)

    for para in doc.paragraphs:
        text += para.text + "\n"

    return text


def extract_text(file):
    filename = file.filename.lower()

    if filename.endswith(".pdf"):
        return extract_text_from_pdf(file)

    elif filename.endswith(".docx"):
        return extract_text_from_docx(file)

    else:
        return "Unsupported file format"