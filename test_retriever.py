from rag.retriever import Retriever

retriever = Retriever()

query = "What technologies are used in the Smart Campus Navigation System?"

results = retriever.retrieve(query)

documents = results["documents"][0]
metadatas = results["metadatas"][0]
distances = results["distances"][0]

print("=" * 80)

for i in range(len(documents)):

    print(f"\nResult {i+1}")

    print(f"Similarity Score: {distances[i]}")

    print(f"Page: {metadatas[i]['page']}")

    print()

    print(documents[i][:400])

    print("-" * 80)