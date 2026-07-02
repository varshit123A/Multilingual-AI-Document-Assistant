from rag.qa_chain import QAChain

qa = QAChain()

question = input("Ask: ")

result = qa.ask(question)

print("\n==============================\n")

print(result["answer"])

print("\nSources:")

print(result["sources"])