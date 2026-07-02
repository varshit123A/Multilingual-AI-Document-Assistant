import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from gtts import gTTS

from rag.ingestion import DocumentIngestion
from rag.qa_chain import QAChain

# -------------------------
# Load Gemini API Key
# -------------------------

load_dotenv()

genai.configure(
    api_key=os.getenv("GOOGLE_API_KEY")
)

model = genai.GenerativeModel("gemini-2.5-flash")

# -------------------------
# Initialize RAG
# -------------------------

ingestion = DocumentIngestion()
qa = QAChain()

# -------------------------
# Streamlit UI
# -------------------------

st.title("📄 Multilingual AI Document Assistant")

uploaded_file = st.file_uploader(
    "Upload a PDF",
    type=["pdf"]
)

if uploaded_file:

    # -------------------------
    # Save PDF
    # -------------------------

    os.makedirs("uploads", exist_ok=True)

    pdf_path = os.path.join(
        "uploads",
        uploaded_file.name
    )

    with open(pdf_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # -------------------------
    # Extract Text
    # -------------------------

    reader = PdfReader(pdf_path)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text

    st.success("✅ PDF Loaded Successfully")

    # -------------------------
    # Index into Vector Database
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

        try:

            summary_prompt = f"""
            Summarize the following document
            in 5 concise bullet points.

            Document:
            {text}
            """

            summary = model.generate_content(summary_prompt)

            st.subheader("Summary")

            st.write(summary.text)

        except Exception as e:
            st.error(e)

    # -------------------------
    # Ask Questions (RAG)
    # -------------------------

    question = st.text_input(
        "Ask a Question about the PDF"
    )

    if st.button("Ask"):

        try:

            with st.spinner("Searching document..."):

                result = qa.ask(question)

            answer = result["answer"]

            st.subheader("Answer")

            st.write(answer)

            st.session_state["answer"] = answer

            st.subheader("Sources")

            for source in result["sources"]:

                st.write(
                    f"📄 Page {source['page'] + 1}"
                )

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

            try:

                translation_prompt = f"""
                Translate the following text into {language}

                Text:
                {st.session_state['answer']}
                """

                translated = model.generate_content(
                    translation_prompt
                )

                st.subheader(
                    f"Translated ({language})"
                )

                st.write(translated.text)

            except Exception as e:

                st.error(e)

        # -------------------------
        # Text To Speech
        # -------------------------

        if st.button("Generate Speech"):

            try:

                tts = gTTS(
                    st.session_state["answer"]
                )

                tts.save("output.mp3")

                st.audio("output.mp3")

            except Exception as e:

                st.error(e)