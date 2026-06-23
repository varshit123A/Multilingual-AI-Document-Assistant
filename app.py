import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from gtts import gTTS
import os

# -------------------------
# Load Gemini API Key
# -------------------------

load_dotenv()

genai.configure(
    api_key=os.getenv("GOOGLE_API_KEY")
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

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
    # Extract PDF Text
    # -------------------------

    reader = PdfReader(uploaded_file)

    text = ""

    for page in reader.pages:

        page_text = page.extract_text()

        if page_text:
            text += page_text

    st.success("✅ PDF Loaded Successfully")

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

            summary = model.generate_content(
                summary_prompt
            )

            st.subheader("Summary")

            st.write(summary.text)

        except Exception as e:

            st.error(f"Error: {e}")

    # -------------------------
    # Ask Question
    # -------------------------

    question = st.text_input(
        "Ask a Question about the PDF"
    )

    answer = ""

    if st.button("Ask"):

        try:

            prompt = f"""
            Document:
            {text}

            Question:
            {question}

            Answer:
            """

            response = model.generate_content(
                prompt
            )

            answer = response.text

            st.subheader("Answer")

            st.write(answer)

            # Store answer
            st.session_state["answer"] = answer

        except Exception as e:

            st.error(f"Error: {e}")

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
                Translate the following text
                into {language}

                Text:
                {st.session_state['answer']}
                """

                translated = model.generate_content(
                    translation_prompt
                )

                st.subheader(
                    f"Translated ({language})"
                )

                st.write(
                    translated.text
                )

            except Exception as e:

                st.error(f"Error: {e}")

        # -------------------------
        # Text To Speech
        # -------------------------

        if st.button("Generate Speech"):

            try:

                tts = gTTS(
                    st.session_state["answer"]
                )

                tts.save(
                    "output.mp3"
                )

                st.audio(
                    "output.mp3"
                )

            except Exception as e:

                st.error(f"Error: {e}")