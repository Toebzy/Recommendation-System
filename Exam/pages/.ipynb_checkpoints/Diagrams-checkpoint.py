import streamlit as st
import pandas as pd
import numpy as np
import random
import webbrowser
import io
from io import StringIO, BytesIO
import matplotlib.pyplot as plt
from urllib.error import URLError
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff
import plotly.io as pio
from PIL import Image
import streamlit.components.v1 as components
from streamlit.components.v1 import html

import sweetviz as sv


import sys, os
import platform
sys.path.append('../')

st.set_page_config(page_title="Diagrams", page_icon="📊")

st.title("Diagrams")
st.sidebar.header("Diagrams", divider='rainbow')

df_q = pd.read_csv('./q_movies.csv', index_col=None, na_values=['NA'])
df_y = pd.read_csv('./year.csv', index_col=None, na_values=['NA'])
df = pd.merge(df_q, df_y[['movieId', 'year_released', 'decade']], on='movieId', how='left')
unique_genres_movies = pd.read_csv('./unique_genres_movies.csv', index_col=None, na_values=['NA'])
mvrt = pd.read_csv('./mvrt.csv', index_col=None, na_values=['NA'])
genre_list = ['Drama', 'Comedy', 'Action', 'Thriller', 'Adventure', 'Romance',
               'Sci-Fi', 'Crime', 'Fantasy', 'Children', 'Mystery', 'Horror',
               'Animation', 'War', 'IMAX', 'Musical', 'Western', 'Documentary', 'Film-Noir']
def eda(df):
    my_report = sv.analyze([df,'EDA'])
    my_report.show_html('html/eda.html', open_browser=False)     
    # components.iframe(src='http://localhost:3001/eda.html', width=1100, height=1200, scrolling=True)                
    return my_report
    
def average_rating_by_genre(data, genre_list):
    
    genres_expanded = data['genres'].str.get_dummies(sep='|')

    # Step 2: Concatenate 'genres_expanded' with 'data'
    data_genres = pd.concat([data, genres_expanded], axis=1)

    # Step 3: Calculate average rating for each genre
    average_ratings = {}
    for genre in genre_list:
        if genre in data_genres.columns:
            average_rating = data_genres[data_genres[genre] == 1]['rating'].mean()
            average_ratings[genre] = average_rating

    return average_ratings

    
# Main 
tab = ''


eda(df)
if st.button(":green[See Diagrams]"):
                average_ratings_by_decade = df.groupby('decade')['average_rating'].mean().reset_index()
                # Streamlit app
                st.title('Average Ratings by Decade')
                fig_decade = px.bar(average_ratings_by_decade, x='decade', y='average_rating')
                fig_decade.update_layout(xaxis_tickangle=-45)  # Rotate x-axis labels
                fig_decade.update_xaxes(title_text='Decade') 
                fig_decade.update_yaxes(title_text='Average Rating') 
                st.plotly_chart(fig_decade)
                       
                result = average_rating_by_genre(mvrt, genre_list)
                result_df = pd.DataFrame(list(result.items()), columns=['Genre', 'Average Rating'])
    
                st.title('Average Ratings by Genre')
                fig_genre = px.bar(result_df, x='Genre', y='Average Rating')
                fig_genre.update_layout(xaxis_tickangle=-45)  # Rotate x-axis labels
                st.plotly_chart(fig_genre)

                st.title('Ratings count')
                fig_rating_count = px.histogram(mvrt, x='rating', nbins=20)
                fig_rating_count.update_traces(marker_line_color='black', marker_line_width=1)
                st.plotly_chart(fig_rating_count)
            
                st.title('Genre Distribution')

                fig_genre_count = px.bar(unique_genres_movies, x='index', y='count')
                fig_genre_count.update_layout(xaxis_tickangle=-45)
                st.plotly_chart(fig_genre_count)

                image = Image.open("./piechart.png")
                # Display the image
                st.image(image, caption='', use_column_width=True)

                st.title('Average Rating Count')
                fig_rating_count = px.histogram(df_q, x='average_rating', nbins=20)
                fig_rating_count.update_traces(marker_line_color='black', marker_line_width=1)
                st.plotly_chart(fig_rating_count)

                image = Image.open("./percentage_genre_year.png")  # Replace with the path to your image file
                st.title('Percentage of genres by 10 years')
                # Display the image
                st.image(image, caption='', use_column_width=True)

                image = Image.open("./scatterplot.png")
                st.title('Relation between Vote Count and Average Rating')
                # Display the image
                st.image(image, caption='', use_column_width=True)
    
if st.button(":blue[EDA]"):
    # st.write(os.getcwd())
    with open("html/eda.html", "r", encoding='utf-8') as f:
        html_data = f.read() 
        components.html(html_data, width=1600, height=1600, scrolling=True)   

        

    

