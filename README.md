
# SHL Assessment Recommendation Agent

An AI-powered conversational recommendation system that helps recruiters and hiring teams discover relevant SHL assessments using semantic search and conversational retrieval.

## Features

- Conversational assessment recommendation
- Semantic search using Sentence Transformers
- FAISS vector similarity search
- Multi-turn conversation support
- Clarification handling for vague queries
- Comparison support for assessments
- Off-topic query rejection
- FastAPI backend with Swagger documentation

---

## Tech Stack

- Python
- FastAPI
- Sentence Transformers
- FAISS
- Pandas
- BeautifulSoup
- Uvicorn

---

## Project Structure

```text
shl-assessment-agent/
│
├── app/
│   ├── main.py
│   ├── agent.py
│   ├── retriever.py
│   └── models.py
│
├── data/
│   └── shl_assessments.csv
│
├── scripts/
│   └── scrape_catalog.py
│
├── requirements.txt
├── README.md
└── .gitignore
````

---

## How It Works

1. SHL catalog data is scraped and stored locally.
2. Assessment descriptions are converted into embeddings.
3. FAISS indexes embeddings for semantic similarity search.
4. User queries are processed through conversational agent logic.
5. Relevant SHL assessments are recommended through API responses.

---

## API Endpoints

### Health Check

```http
GET /health
```

### Chat Endpoint

```http
POST /chat
```

Example Request:

```json
{
  "messages": [
    {
      "role": "user",
      "content": "Hiring backend engineer with Java and API skills"
    }
  ]
}
```

---

## Running Locally

Install dependencies:

```bash
pip install -r requirements.txt
```

Run server:

```bash
uvicorn app.main:app --reload
```

Open Swagger UI:

```text
http://127.0.0.1:8000/docs
```

---

## Future Improvements

* LLM-powered reasoning
* Better assessment metadata extraction
* Advanced comparison explanations
* Persistent vector database
* Authentication and user sessions

```

