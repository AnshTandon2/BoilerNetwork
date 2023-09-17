import PyPDF2

def extract_text_from_pdf(pdf_file):
    text = ''
    try:
        with open(pdf_file, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfFileReader(pdf_file)
            for page in range(pdf_reader.getNumPages()):
                text += pdf_reader.getPage(page).extractText()
    except Exception as e:
        print(f"Error extracting text from PDF: {e}")
    
    return text

def main():
    resume_file = 'sample_resume.pdf'  # Replace with the path to your PDF resume file
    
    text = extract_text_from_pdf(resume_file)
    print(text)  # This will print the extracted text from the PDF resume

if __name__ == "__main__":
    main()
