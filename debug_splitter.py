from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

text = "Hello World " * 500

doc = Document(page_content=text)

splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
)

chunks = splitter.split_documents([doc])

print("Text Length:", len(text))
print("Chunks:", len(chunks))