import streamlit as st
import pandas as pd
import numpy as np
import random
import webbrowser
import io
from io import StringIO, BytesIO
from sklearn.feature_extraction.text import TfidfVectorizer
import base64
import graphviz
from sklearn import datasets, preprocessing, metrics
from sklearn import tree
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics.pairwise import linear_kernel
from urllib.error import URLError
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff
import plotly.io as pio
from sklearn.metrics.pairwise import linear_kernel
import streamlit.components.v1 as components
from streamlit.components.v1 import html

import sweetviz as sv

from sklearn.metrics.pairwise import cosine_similarity
from sklearn.model_selection import train_test_split
from scipy.sparse import coo_matrix
from sklearn.metrics import mean_squared_error
import seaborn as sns

import sys, os
import platform
sys.path.append('../')

st.set_page_config(page_title="BI Exam", page_icon="📊")

st.title("Recommend movies by User")
st.sidebar.header("Recommend movies by User", divider='rainbow')
movies = pd.read_csv('./q_movies.csv', index_col=None, na_values=['NA'])

df = pd.read_csv('./movies.csv', index_col=None, na_values=['NA'])
mvrt = pd.read_csv('./mvrt.csv', index_col=None, na_values=['NA'])
mvrt_train=mvrt

user_movie_matrix = mvrt_train.pivot_table(index='userId', columns='movieId', values='rating', fill_value=0)
user_movie_array = user_movie_matrix.to_numpy()
train_data, test_data = train_test_split(user_movie_array, test_size=0.2, random_state=42)
data = train_data

def viz2():

    x = int(st.number_input("Choose a userid 1-487", format="%f"))
    return x
    


class CollaborativeFilteringRecommender:
    def __init__(self, n_neighbors=5):
        self.n_neighbors = n_neighbors
        self.user_similarity = None

    def fit(self, train_data):
        # Compute user-user similarity matrix using cosine similarity
        self.user_similarity = cosine_similarity(train_data)

    def predict(self, user_indices, train_data):
        # Compute weighted average of ratings from similar users for each user index
        recommendations = []
        for user_index in user_indices:
            user_sim_scores = self.user_similarity[user_index]
            top_sim_users = np.argsort(user_sim_scores)[-self.n_neighbors - 1:-1]  # Exclude the user itself

            user_ratings = train_data[top_sim_users, :]
            user_sim_scores = user_sim_scores[top_sim_users]

            # Weighted average of ratings from similar users
            pred_ratings = np.dot(user_sim_scores, user_ratings) / np.sum(user_sim_scores)
            recommendations.append(pred_ratings)

        return recommendations

recommender = CollaborativeFilteringRecommender(n_neighbors=5)
recommender.fit(data)



def predict_for_user(user_indices, mvrt, recommendations):
    user_results = []

    for i, user_index in enumerate(user_indices):
        user_result = {
            'user_id': user_index,
            'known_positives': [],
            'recommended': []
        }

        known_positives = mvrt[(mvrt['userId'] == user_index) & (mvrt['rating'] > 4)].nlargest(3, 'rating')
        for _, row in known_positives.iterrows():
            user_result['known_positives'].append(row['title'])

        for item_index in recommendations[i].argsort()[-3:][::-1]:
            movie_id = mvrt['movieId'].unique()[item_index]
            movie_title = mvrt[mvrt['movieId'] == movie_id]['title'].iloc[0]
            user_result['recommended'].append(movie_title)

        user_results.append(user_result)

    return user_results
    # Make predictions for the test set
    test_predictions = recommender.predict(range(len(test_data)), train_data)

    # Calculate mean squared error
    mse = mean_squared_error(test_data, test_predictions)
    print("Mean Squared Error:", mse)
# Main 
tab = ''
# tab = '../data/shopping-data.csv'


x = viz2()
if st.button(":green[Get Recommendations]"):
     user_indices = [x]
     recommendations = recommender.predict(user_indices, data)
     user_results = predict_for_user(user_indices, mvrt, recommendations)

     for result in user_results:

        st.subheader("This user likes:")
        for positive in result['known_positives']:
            st.write(f"    {positive}")

        st.subheader("We think you will also like:")
        for recommended_movie in result['recommended']:
            st.write(f"    {recommended_movie}")
    
    

            
        

    

