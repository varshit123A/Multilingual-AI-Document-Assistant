import os
import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from gtts import gTTS

from langchain_google_genai import ChatGoogleGenerativeAI

from rag.ingestion import DocumentIngestion
from rag.qa_chain import QAChain

# -------------------------
# Load Environment Variables
# -------------------------

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0,
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

# -------------------------
# Initialize RAG
# -------------------------

ingestion = DocumentIngestion()
qa = QAChain()

# -------------------------
# Streamlit UI
# -------------------------

st.set_page_config(
    page_title="Multilingual AI Document Assistant",
    page_icon="📄"
)

st.title("📄 Multilingual AI Document Assistant")

uploaded_file = st.file_uploader(
    "Upload a PDF",
    type=["pdf"]
)

if uploaded_file:

    os.makedirs("uploads", exist_ok=True)

    pdf_path = os.path.join(
        "uploads",
        uploaded_file.name
    )

    with open(pdf_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # -------------------------
    # Extract PDF Text
    # -------------------------

    reader = PdfReader(pdf_path)

    text = ""

    for page in reader.pages:

        page_text = page.extract_text()

        if page_text:
            text += page_text

    st.success("✅ PDF Loaded Successfully")

    # -------------------------
    # Index Document
    # -------------------------

    with st.spinner("Indexing document..."):

        chunks = ingestion.ingest(pdf_path)

    if chunks == 0:
        st.info("Document already indexed.")
    else:
        st.success(f"Indexed {chunks} chunks successfully.")

    # -------------------------
    # Summarize PDF
    # -------------------------

    if st.button("📌 Summarize PDF"):

        prompt = f"""
Summarize the following document in 5 concise bullet points.

Document:
{text}
"""

        try:

            response = llm.invoke(prompt)

            st.subheader("Summary")

            st.write(response.content)

        except Exception as e:

            st.error(e)

    # -------------------------
    # Ask Question
    # -------------------------

    question = st.text_input(
        "Ask a Question about the PDF"
    )

    if st.button("Ask"):

        if question.strip() == "":
            st.warning("Please enter a question.")

        else:

            try:

                with st.spinner("Searching document..."):

                    result = qa.ask(question)

                answer = result["answer"]

                st.subheader("Answer")

                st.write(answer)

                st.session_state["answer"] = answer

                st.subheader("Source Pages")

                for page in result["sources"]:
                    st.write(f"📄 Page {page}")

            except Exception as e:

                st.error(e)

    # -------------------------
    # Translation
    # -------------------------

    if "answer" in st.session_state:

        language = st.selectbox(
            "Translate To",
            [
                "Telugu",
                "Hindi",
                "Tamil",
                "Kannada",
                "Malayalam"
            ]
        )

        if st.button("Translate"):

            prompt = f"""
Translate the following text into {language}.

Text:
{st.session_state["answer"]}
"""

            try:

                translated = llm.invoke(prompt)

                st.subheader(f"Translated ({language})")

                st.write(translated.content)

            except Exception as e:

                st.error(e)

        # -------------------------
        # Text To Speech
        # -------------------------

        if st.button("Generate Speech"):

            try:

                tts = gTTS(st.session_state["answer"])

                tts.save("output.mp3")

                st.audio("output.mp3")

            except Exception as e:

                st.error(e)