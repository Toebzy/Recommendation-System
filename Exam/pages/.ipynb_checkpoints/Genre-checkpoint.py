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


import sys, os
import platform
sys.path.append('../')

st.set_page_config(page_title="BI Exam", page_icon="📊")

st.title("Recommend movies by genre")
st.sidebar.header("Recommend movies by genre", divider='rainbow')

def viz2():
        x = st.text_input("Enter Genre. If more than one genre is wanted, seperate genres by |")
        return x
    
movies = pd.read_csv('./q_movies.csv', index_col=None, na_values=['NA'])
df = pd.read_csv('./movies.csv', index_col=None, na_values=['NA'])
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(movies['genres'])
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
indices = pd.Series(movies.index, index=movies['genres']).drop_duplicates()

def get_recommendations(genre, cosine_sim=cosine_sim):
        # Get the indices of movies with the specified genre
        genre_list = genre.split('|')
        sorted_genre_list = sorted(genre_list)
        separator = '|'
        genre = separator.join(sorted_genre_list)
        genre_indices = indices[indices.index.str.contains(genre, case=False)]

        # Initialize an empty list to store similarity scores
        sim_scores = []

        # Iterate over the genre indices and get the cosine similarity scores
        for idx in genre_indices:
            sim_scores.extend(list(enumerate(cosine_sim[idx])))

        # Sort the movies based on the similarity scores
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

        # Get the scores of the 10 most similar movies
        sim_scores = sim_scores[1:11]

        # Get the movie indices
        movie_indices = [i[0] for i in sim_scores]

        # Return the top 10 most similar movies
        movies_with_score = movies[['title', 'genres', 'score']].iloc[movie_indices]
        filtered_movies = movies_with_score[(movies_with_score['score'] > 0) & movies_with_score['genres'].apply(lambda x: all(genre in x for genre in sorted_genre_list))]
        sorted_movies = filtered_movies.sort_values(by='score', ascending=False)
        return sorted_movies.drop_duplicates(subset='title').head(5)

# Main 
tab = ''
# tab = '../data/shopping-data.csv'


x = viz2()
if st.button(":green[Get Recommendations]"):
            st.subheader("We Recommend")
            st.write(get_recommendations(x))
if st.button(":green[See all Genres]"):
            st.subheader("Genres")
            st.write(
'Drama,',          
'Comedy,',         
'Action,',         
'Thriller,',       
'Adventure,',      
'Romance,',        
'Sci-Fi,',         
'Crime,',          
'Fantasy,',       
'Children,',        
'Mystery,',         
'Horror,',          
'Animation,',       
'War,',             
'IMAX,',            
'Musical,',         
'Western,',         
'Documentary,',    
'Film-Noir')           
    
            
    

            
        

    

