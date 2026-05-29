import fitz

def extract_pdf_text(pdf_file):

    text = ""

    doc = fitz.open(
        stream=pdf_file.read(),
        filetype="pdf"
    )

    for page in doc:
        text += page.get_text()

    return text