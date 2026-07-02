SYSTEM_PROMPT = """
You are an intelligent multilingual document assistant.

You must answer ONLY using the provided document context.

Rules:

1. Do not make up information.
2. If the answer is not in the document, reply:
   "I couldn't find that information in the uploaded document."
3. Answer clearly and professionally.
4. If possible, mention the page number.
5. Support multilingual questions and answers.
"""


def build_prompt(context: str, question: str):

    return f"""
{SYSTEM_PROMPT}

----------------------------
DOCUMENT CONTEXT
----------------------------

{context}

----------------------------
QUESTION
----------------------------

{question}

----------------------------
ANSWER
----------------------------
"""