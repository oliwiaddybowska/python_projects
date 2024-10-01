import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def performUserBasedCF(ratingMatrix, targetUserIndex, N, K):
    # calculate cosine similarity between users
    userSimilarityMatrix = cosine_similarity(ratingMatrix)
    np.fill_diagonal(userSimilarityMatrix, 0)

    # select similar users with target user
    lstSimilarity = userSimilarityMatrix[targetUserIndex]
    lstSimilarUsers = np.argsort(-lstSimilarity)[:K]    # top-K similar users

    # find recommended movies
    recommendations = []
    for movieIndex, movieTitle in enumerate(ratingMatrix.columns):
        # exclude already watched movies
        if ratingMatrix.iat[targetUserIndex, movieIndex] == 0:
            # calculate the predicted rating by weighted average
            valueSum = 0
            weightSum = 0
            for neighbor in lstSimilarUsers:
                valueSum += ratingMatrix.iat[neighbor, movieIndex] * lstSimilarity[neighbor]
                weightSum += lstSimilarity[neighbor]
            recommendations.append((movieTitle, valueSum / weightSum))

    # sort the recommendations by rating in descending order
    recommendations.sort(key=lambda x: x[1], reverse=True)
    top_n_recommendations = recommendations[:N]

    return top_n_recommendations


rawRatings = pd.read_csv('ratings.csv')
rawMovies = pd.read_csv('movies.csv')

rawData = pd.merge(rawRatings, rawMovies, on = 'movieId')

userMovieRating = rawData.pivot_table('rating', index = 'userId', columns='title')
userMovieRating.fillna(0, inplace = True)

targetUserIndex = 609   # 0 ~ 609
N = 10
K = 5

top_n_recommendations = performUserBasedCF(userMovieRating, targetUserIndex, N, K)

# display the list of recommended movies for the user
print(f"Top {N} movie recommendations for User {targetUserIndex + 1}:")
for movie_title, predicted_rating in top_n_recommendations:
    print(f"{movie_title} (Predicted Rating: {predicted_rating:.2f})")