FROM python:3.10-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Download NLTK stopwords
RUN python -m nltk.downloader stopwords

# Copy source code and data
COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
