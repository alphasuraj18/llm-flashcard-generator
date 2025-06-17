import PyPDF2

def extract_text_from_pdf(uploaded_file):
    reader = PyPDF2.PdfReader(uploaded_file)
    return "\n".join(page.extract_text() for page in reader.pages if page.extract_text())
