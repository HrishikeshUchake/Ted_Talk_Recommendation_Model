FROM python:3.10-slim

WORKDIR /app

# System-level dependencies for wordcloud & matplotlib
RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    python3-dev \
    libfreetype6-dev \
    libpng-dev \
    libjpeg-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python packages
COPY requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Download stopwords for nltk
RUN python -m nltk.downloader stopwords

# Copy project files
COPY . .

EXPOSE 8501

# Use full path to Streamlit
ENTRYPOINT ["python", "-m", "streamlit", "run", "streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"]
