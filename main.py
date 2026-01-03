import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

ratings = pd.read_csv(r"C:\Users\ruchi\Downloads\ml-100k\ml-100k\u.data", sep="\t", names=["userId", "movieId", "rating", "timestamp"])
# ratings.to_csv("ratings.csv", index=False)

columns = ["movieId", "title", "release_date", "video_release_date", "IMDb_URL"]
# plus a bunch of genre columns if you want them
movies = pd.read_csv(r"C:\Users\ruchi\Downloads\ml-100k\ml-100k\u.item", sep="|", names=columns + list(range(19)), encoding='latin-1')
# movies.to_csv("movies.csv", index=False)
movies = pd.read_csv(r"C:\Users\ruchi\OneDrive\Desktop\GitDemo\Movie-Recommendation-System\movies.csv")
ratings = pd.read_csv(r"C:\Users\ruchi\OneDrive\Desktop\GitDemo\Movie-Recommendation-System\ratings.csv")

data = ratings.merge(movies, on='movieId')

movie_matrix = data.pivot_table(index='title', columns='userId', values='rating')

movie_matrix_filled = movie_matrix.fillna(0)

# Compute similarity between movies
similarity = cosine_similarity(movie_matrix_filled)
similarity_df = pd.DataFrame(similarity, index=movie_matrix.index, columns=movie_matrix.index)

def recommend_movies(movie_name, top_n=5):
    similar_movies = similarity_df[movie_name].sort_values(ascending=False)
    recommendations = similar_movies.iloc[1:top_n+1]
    return recommendations

# Example:
print(recommend_movies("Toy Story (1995)"))

import matplotlib.pyplot as plt

recommendations = recommend_movies("Toy Story (1995)")
recommendations.plot(kind='barh', figsize=(8,5))
plt.show()
