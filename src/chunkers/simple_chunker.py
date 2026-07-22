class SimpleChunker:
    def __init__(self, chunk_size=500):
        self.chunk_size = chunk_size

    def chunk(self, pages):
        chunks = []

        for page in pages:
            text = page["text"]

            for i in range(0, len(text), self.chunk_size):
                chunks.append({
                    "page": page["page"],
                    "text": text[i:i+self.chunk_size]
                })

        return chunks