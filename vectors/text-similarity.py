import numpy as np
import pandas as pd

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


texts = [
    "machine learning model predicts data",
    "data model learns patterns with machine learning",
    "pizza pasta cheese tasty food",
    "tasty food includes pizza and pasta",
    "football team won the match"
]

doc_names = ["doc1_ML", "doc2_ML", "doc3_food", "doc4_food", "doc5_football"]

vectorizer = CountVectorizer(stop_words='english')

X = vectorizer.fit_transform(texts)

words = vectorizer.get_feature_names_out()

bow_table = pd.DataFrame(
    X.toarray(),
    columns=words,
    index=doc_names
)

cos_matrix = cosine_similarity(X)

print("Bag of Word table:")
print(bow_table)
print(cos_matrix)