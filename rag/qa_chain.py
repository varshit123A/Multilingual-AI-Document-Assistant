import os

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

from rag.prompt import build_prompt
from rag.retriever import Retriever

load_dotenv()


class QAChain:
    """
    Complete RAG Question Answering Pipeline
    """

    def __init__(self):

        self.retriever = Retriever()

        self.llm = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash",
            temperature=0,
            google_api_key=os.getenv("GOOGLE_API_KEY")
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

        response = self.llm.invoke(prompt)

        return {
            "answer": response.content,
            "sources": sorted(set(sources))
        }