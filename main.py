import pandas as pd

ratings = pd.read_csv(r"C:\Users\ruchi\Downloads\ml-100k\ml-100k\u.data", sep="\t", names=["userId", "movieId", "rating", "timestamp"])
ratings.to_csv("ratings.csv", index=False)
