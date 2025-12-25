import pandas as pd

ratings = pd.read_csv(r"C:\Users\ruchi\Downloads\ml-100k\ml-100k\u.data", sep="\t", names=["userId", "movieId", "rating", "timestamp"])
# ratings.to_csv("ratings.csv", index=False)

columns = ["movieId", "title", "release_date", "video_release_date", "IMDb_URL"]
# plus a bunch of genre columns if you want them
movies = pd.read_csv(r"C:\Users\ruchi\Downloads\ml-100k\ml-100k\u.item", sep="|", names=columns + list(range(19)), encoding='latin-1')
# movies.to_csv("movies.csv", index=False)
movies = pd.read_csv("movies.csv")
ratings = pd.read_csv("ratings.csv")

data = ratings.merge(movies, on='movieId')
movie_matrix = data.pivot_table(index='title', columns='userId', values='rating')
print(movie_matrix.head())