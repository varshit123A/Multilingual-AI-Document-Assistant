import os

from dotenv import load_dotenv
import google.generativeai as genai

from rag.prompt import build_prompt
from rag.retriever import Retriever

load_dotenv()

genai.configure(
    api_key=os.getenv("GOOGLE_API_KEY")
)


class QAChain:
    """
    Complete RAG Question Answering Pipeline
    """

    def __init__(self):

        self.retriever = Retriever()

        self.model = genai.GenerativeModel(
            "gemini-2.5-flash"
        )

    def ask(self, question):

        results = self.retriever.retrieve(question)

        documents = results["documents"][0]
        metadatas = results["metadatas"][0]

        context = ""

        sources = []

        for doc, meta in zip(documents, metadatas):

            page = meta.get("page", 0)

            context += f"\n(Page {page + 1})\n"
            context += doc + "\n\n"

            sources.append(page + 1)

        prompt = build_prompt(
            context=context,
            question=question
        )

        response = self.model.generate_content(prompt)

        return {
            "answer": response.text,
            "sources": sorted(set(sources))
        }