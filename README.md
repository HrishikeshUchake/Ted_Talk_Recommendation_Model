# TED Talk Recommender

A machine learning-powered web app that recommends similar TED Talks based on user-inputted topics. Built with Streamlit, NLP, and deployed using Docker.

The model converts the user input into a TF-IDF vector and makes decisions based on the cosine similarity and Pearson correlation between the input vector and the dataset, and returns the TED talk that has the highest similarity. 

---

## Features

- NLP-based TED Talk recommendation using TF-IDF and cosine similarity
- Text cleaning with stopwords and punctuation removal
- Web interface using Streamlit
- Fully containerized with Docker for cross-platform deployment

---

## How to Use (Locally with Docker)

### 1. Pull the Docker Image

```bash
docker pull hrishikeshuchake/ted-streamlit

docker run -p 8501:8501 hrishikeshu/ted-streamlit
```

Visit: http://localhost:8501
