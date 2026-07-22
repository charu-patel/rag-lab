from src.loaders.pdf_loader import PDFLoader
from src.chunkers.simple_chunker import SimpleChunker

loader = PDFLoader("data/raw/major_report _final.pdf")
pages = loader.load()

chunker = SimpleChunker(chunk_size=500)
chunks = chunker.chunk(pages)

print(f"Pages: {len(pages)}")
print(f"Chunks: {len(chunks)}")

print("\nFirst Chunk:")
print(chunks[0])

print("\nLast Chunk:")
print(chunks[-1])