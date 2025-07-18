# TED Talk Recommender

A content-based machine learning application that recommends relevant TED Talks based on user-input topics. Built using **NLP techniques**, a **Streamlit web interface**, and deployed via **Docker** for cross-platform accessibility.

This project leverages **TF-IDF vectorization** and **cosine similarity** to identify and recommend talks similar to the user's idea or interest.

---

## Features

-  **Content-Based Recommendation** using TF-IDF and cosine similarity
-  **Text Preprocessing** with tokenization, stopword and punctuation removal (NLTK)
-  **Interactive Web App** built with Streamlit for real-time querying
-  **Dockerized Deployment** for seamless local setup across platforms
-  **Data Visualizations** using WordCloud and matplotlib for dataset insights

---

## Tech Stack

- **Python**, **NLTK**, **scikit-learn**, **pandas**
- **Streamlit** for frontend UI
- **Docker** for deployment
- **matplotlib**, **WordCloud** for exploratory analysis

---

## 📦 Run Locally with Docker

### Step 1: Pull the Docker image

```bash
docker pull hrishikeshuchake/ted-streamlit
````

### Step 2: Run the container

```bash
docker run -p 8501:8501 hrishikeshuchake/ted-streamlit
```

Then open your browser and visit: [http://localhost:8501](http://localhost:8501)

---

## 📁 Dataset

This app uses a cleaned dataset of TED Talk transcripts and metadata from Kaggle, preprocessed for NLP. The input is vectorized using **TF-IDF**, and similar talks are identified using **cosine similarity** and **Pearson correlation**.

---


## 📄 License

MIT License. Feel free to fork, adapt, and build on top of it!

---

## 👤 Author

Developed by [Hrishikesh Uchake](https://github.com/HrishikeshUchake)


