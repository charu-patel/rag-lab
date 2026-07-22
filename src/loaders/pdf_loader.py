import fitz

class PDFLoader:
    def __init__(self, pdf_path):
        self.pdf_path = pdf_path

    def load(self):
        document = fitz.open(self.pdf_path)
        pages = []

        for page_number, page in enumerate(document):
            pages.append({
                "page": page_number + 1,
                "text": page.get_text()
            })

        return pages

#loading padf pages

if __name__ == "__main__":
    loader = PDFLoader("data/raw/major_report _final.pdf")

    pages = loader.load()

    print(len(pages))
    print(pages[0]["page"])
    print(pages[0]["text"][:300])