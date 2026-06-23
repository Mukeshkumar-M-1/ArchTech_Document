import pypdf

def main():
    pdf_path = r"SRS_DEMO_SECTION\SRS_TEST_2.pdf"
    reader = pypdf.PdfReader(pdf_path)
    print(f"Total pages: {len(reader.pages)}")
    
    for i, page in enumerate(reader.pages):
        text = page.extract_text()
        first_few_lines = [line.strip() for line in text.split('\n') if line.strip()][:5]
        print(f"--- Page {i+1} ---")
        for line in first_few_lines:
            print(f"  {line}")

if __name__ == '__main__':
    main()
