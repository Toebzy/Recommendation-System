import streamlit as st
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

import sys, os
import platform
sys.path.append('../')

st.set_page_config(page_title="BI Exam", page_icon="📊")

st.title("Recommend movies by movies")
st.sidebar.header("Recommend movies by movies", divider='rainbow')

# Load data (replace with your actual data paths)
movies = pd.read_csv('./q_movies.csv', index_col=None, na_values=['NA'])
mvrt = pd.read_csv('./mvrt.csv', index_col=None, na_values=['NA'])

# Create movie-user matrix
movie_user_matrix = mvrt.pivot_table(index='userId', columns='movieId', values='rating', fill_value=0)
movie_user_array = movie_user_matrix.to_numpy()

# Compute user-user similarity
user_similarity = cosine_similarity(movie_user_array)

# Function to recommend movies based on selected movie titles
def recommend_movies(selected_titles, user_similarity, movie_id_to_title):
    selected_movie_ids = [title_to_movie_id.get(title) for title in selected_titles if title in title_to_movie_id]

    if len(selected_movie_ids) != 3:
        st.error("Please select exactly 3 movies.")
        return []

    # Find users who rated selected movies
    similar_users = set()
    for movie_id in selected_movie_ids:
        users_rated_high = movie_user_matrix.index[movie_user_matrix[movie_id] > 4]  
        similar_users.update(users_rated_high)

    similar_users = list(similar_users)

    if len(similar_users) == 0:
        st.error("No similar users found based on selected movies. Try different selections.")
        return []

    # Validate user IDs within bounds
    similar_users = [user_id for user_id in similar_users if user_id < user_similarity.shape[0]]

    if len(similar_users) == 0:
        st.error("No valid similar users found based on selected movies. Try different selections.")
        return []

    # Compute average similarity of each user to selected movies
    avg_similarity = np.mean(user_similarity[similar_users, :], axis=0)

    # Sort indices by descending order of similarity
    sorted_indices = np.argsort(avg_similarity)[::-1]

    # Find movies highly rated by similar users
    recommended_movie_ids = set()
    for user_id in similar_users:
        user_ratings = movie_user_matrix.loc[user_id]
        top_movies = user_ratings[user_ratings > 4].index
        recommended_movie_ids.update(top_movies)
        if len(recommended_movie_ids) >= 10:  # Recommend up to 10 movies
            break

    # Exclude selected movies from recommendations
    recommended_movie_ids = list(recommended_movie_ids - set(selected_movie_ids))

    # Filter out movie IDs that are not in movie_id_to_title
    recommended_movies = []
    for movie_id in recommended_movie_ids[:3]:  # Return top 3 recommendations
        if movie_id in movie_id_to_title:
            recommended_movies.append(movie_id_to_title[movie_id])

    if len(recommended_movies) == 0:
        st.error("No recommendations found based on selected movies. Try different selections.")

    return recommended_movies[:3] 

# Mapping of movieId to movie titles
movie_id_to_title = dict(zip(movies['movieId'], movies['title']))
title_to_movie_id = {v: k for k, v in movie_id_to_title.items()}

selected_titles = st.multiselect("Select 3 movies you like:", movies['title'].tolist())

if len(selected_titles) == 3:
    recommendations = recommend_movies(selected_titles, user_similarity, movie_id_to_title)

    if recommendations:
        st.subheader("Movies you might like:")
        for movie in recommendations:
            st.write(f"- {movie}")
else:
    if len(selected_titles) > 0:
        st.error("Please select exactly 3 movies.")
