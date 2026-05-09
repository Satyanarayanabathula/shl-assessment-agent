import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


df = pd.read_csv("data/shl_assessments.csv")

documents = (
    df["name"].fillna("") + " " +
    df["description"].fillna("")
)

vectorizer = TfidfVectorizer()

tfidf_matrix = vectorizer.fit_transform(documents)


def retrieve_assessments(query, top_k=5):

    query_vector = vectorizer.transform([query])

    similarities = cosine_similarity(
        query_vector,
        tfidf_matrix
    ).flatten()

    top_indices = similarities.argsort()[-top_k:][::-1]

    results = []

    for idx in top_indices:

        results.append({
            "name": df.iloc[idx]["name"],
            "url": df.iloc[idx]["url"],
            "description": df.iloc[idx]["description"]
        })

    return results
