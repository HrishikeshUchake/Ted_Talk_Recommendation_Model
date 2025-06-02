# import necessary libraries

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import nltk
import string
import warnings
from scipy.stats import pearsonr
from nltk.corpus import stopwords
from wordcloud import WordCloud
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nltk.download('stopwords')
warnings.filterwarnings('ignore')

# Load the dataset

df = pd.read_csv('tedx_dataset.csv')
print(df.head())

# Data Preprocessing
df.shape
df.isnull().sum()

splitted = df['posted'].str.split(' ', expand=True)

# Creating columns for month and year of the talk
df['year'] = splitted[2].astype('int')
df['month'] = splitted[1]

df['year'].value_counts().plot.bar()
plt.show()

# Combining the title and the details of the talk.
df['details'] = df['title'] + ' ' + df['details']

# Removing the unnecessary information
df = df[['main_speaker', 'details']]
df.dropna(inplace = True)
df.head()

# Making a copy of this data for future use.
data = df.copy()


# Removing punctuation and stopwords
def remove_stopwords(text):
  stop_words = stopwords.words('english')

  imp_words = []

  # Storing the important words
  for word in str(text).split():
    word = word.lower()

    if word not in stop_words:
      imp_words.append(word)

  output = " ".join(imp_words)

  return output


# Applying the function to the details column
df['details'] = df['details'].apply(lambda text: remove_stopwords(text))
df.head()

# Removing punctuations
punctuations_list = string.punctuation


# Function to remove punctuations from the text
def cleaning_punctuations(text):
	signal = str.maketrans('', '', punctuations_list)
	return text.translate(signal)


# Applying the function to the details column
df['details'] = df['details'].apply(lambda x: cleaning_punctuations(x))
df.head()

# Creating a word cloud to visualize the most common words in the details column
details_corpus = " ".join(df['details'])

plt.figure(figsize=(20, 20))
wc = WordCloud(max_words=1000,
			width=800,
			height=400).generate(details_corpus)
plt.axis('off')
plt.imshow(wc)
plt.show()

# Creating a TF-IDF Vectorizer
vectorizer = TfidfVectorizer(analyzer = 'word')
vectorizer.fit(df['details'])