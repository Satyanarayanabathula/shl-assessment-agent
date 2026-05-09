import pandas as pd
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# load dataset
df = pd.read_csv("data/shl_assessments.csv")

# load embedding model
model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

# prepare documents
documents = (
    df["name"].fillna("") + " " +
    df["description"].fillna("")
).tolist()



# create embeddings
embeddings = model.encode(
    documents,
    show_progress_bar=True
)

embeddings = np.array(embeddings)

# create FAISS index
dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)

index.add(embeddings)

print("RETRIEVER READY")


def retrieve_assessments(query, top_k=5):

    query_embedding = model.encode([query])

    D, I = index.search(
        np.array(query_embedding),
        top_k
    )

    results = []

    for idx in I[0]:

        assessment = {
            "name": df.iloc[idx]["name"],
            "url": df.iloc[idx]["url"],
            "description": df.iloc[idx]["description"][:300]
        }

        results.append(assessment)

    return results


if __name__ == "__main__":

    query = "Java backend developer"

    results = retrieve_assessments(query)

    for result in results:

        print(result["name"])
        print(result["url"])
        print("-" * 50)