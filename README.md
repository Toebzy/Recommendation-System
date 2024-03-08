# Recommendation-System - BI Exam Project 
![2022_01_Untitled-design-16](https://github.com/Toebzy/Recommendation-System/assets/113095884/6880aebb-c750-4aaa-b0e3-d16b21d94ce4)

## Problem Formulation

In today’s digital era, users are presented with vast amounts of content and choices across various online sites. Using machine learning, we can create a system that helps customers discover relevant content, by providing individualized recommendations. This way, we help the user avoid information overload, which in turn helps create sales and increases company profits.

## Choices 
We had some issues when it came to forming a recommendation. The problem was due to the size of our dataset. Many of the movies had very few or only 1 review. 
This made it difficult to make an average rating for recommendation. We found several larger datasets, but so large that it brought technical issues. 
We decided to use the upper 10th quantile of total votes. This let us have 900+ movies with a minimum of 27 votes. 

## Theoretical Foundation
We needed to decide what to recommend the user, based on existing user data. Based on our dataset, this came to be the average of rating per movie based on your liked genres. 
However, there is no defenitive way to recommend movies perfectly. Users might like something more than highly rated movies, since critics and user reviews often dont share the same views on entertainment. 
We therefore decidet to developed a more advanced algorithm, that takes a users similarities and recommends movies based on simalar users ratings. This should give more accuruate recommendations based on the previous theory. 

## Results
Our user recommendation function, works by recommending highly rated titles of the same genre. We can get anything meaningful out of this, due to our inability to test it with user surveys. 
The other recomendation system is more advanced, and works on more than just similar genres. Therefore we can also value the response with an accuracy. 
## Streamlit
To open the Streamlit app open a terminal/console on the Exam folder and type streamlit run overview.py
#

Tobias Carlsen - cph-tc183@cphbusiness.dk

Christian Kortsen - cph-cc283@cphbusiness.dk

Daniel Trelborg - cph-dh216@cphbusiness.dk

Simone Toft Hansen - cph-sh575@cphbusiness.dk
