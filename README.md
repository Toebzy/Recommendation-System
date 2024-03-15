# Recommendation-System - BI Exam Project 

![2022_01_Untitled-design-16](https://github.com/Toebzy/Recommendation-System/assets/113095884/6880aebb-c750-4aaa-b0e3-d16b21d94ce4)

## Problem Formulation

In today’s digital era, users are presented with vast amounts of content and choices across various online sites. Using machine learning, we can create a system that helps customers discover relevant content, by providing individualized recommendations. This way, we help the user avoid information overload, which in turn helps create sales and increases company profits.

## Choices 
We encountered issues with Jupyter Notebook crashing, which we traced back to our large dataset. After conducting research, we discovered that the problem stemmed from the dataset's size, consisting of millions of rows. To address this, we opted to use a smaller version of our dataset. While this meant having less data than desired, we believe that the recommendations we generate remain robust and usable.  

We designed the code to be adaptable for potential future use with a larger dataset. If we acquire software capable of handling larger datasets, the only necessary modification would be updating the file path.  

Additionally, we faced the challenge with our content based recommender of deciding which movies to recommend. Many films in our dataset had one or fewer reviews, making it impractical to base recommendations on such limited feedback. To address this, we opted to generate recommendations based on movies in the upper 10th quantile. This criterion ensures that all recommended movies have received at least 27 reviews. While our dataset still contained 100,000 ratings, we had hoped to work with an even larger dataset for more comprehensive results.  

For our collaborative filtering system we used a sparse matrix and figured this could be throwing off recommendations and therefore created another collaborative filtering system using singular value decomposition to decompose the user-item matrix since SVD is less sensitive to sparse data

We originally wanted to create a hybrid system between content-based and collaborative filtering using gradient descent and matrix factorization, but Jupyter Notebook ran into memory issues and was unable to run it.

## Theoretical Foundation
There are many different types of recommendation systems and we decided to create two different types, content-based and collaborative filtering.
Four our content-based system we first needed to decide what variables we would recommend based on. Based on our dataset, we decided on the WAR (weighted average rating) movie and a genre of your choice, we then developed a function using NLP and Text Vectorization, checking the cosine similarity and then ranking by WAR to recommend movies. 
With content-based systems the main problem you run into is that you don't get to show the user something different, the recommendation will always be based on what we know the user likes and means you end up recommending a lot of similar items. This is why we decided to also make a collaborative filtering system, where we find users that are similar to our user and make recommendations based on the WAR of movies based on the most similar users ratings. This was done by creating a user-item matrix and utilizing cosine similarity to create a similarity matrix between users. 

## User Research
### User 1
Han synes det var forståeligt og ligetil.  
Kunne nemt forstå dataen der blev vist.

### User 2
Forklaring på siderne, siden han har glemt det efter diagrammerne er loaded. Mere tekst ud fra diagrammerne der forklarer hvad han kigger på og hvad det er baseret ud fra. 
Kan laves lidt pænere at kigge på, hvis der er fokus på det.
I stedet for “recommended”, så “recommended to this user”. Igen kan det forklares og vises lidt mere tydeligt hvis man ikke har en der kan forklare hvad ting betyder. 
“It does what I think it would do, straightforward”.

### User 3
Diagram texten er svær at læse, siden det står lodret. Ville være rart hvis det var vinklet. 
Det er nemt og overskueligt at læse. Det kunne være rart at vide hvor mange ratings gennemsnittet er baseret på. Det kunne være rart at kunne være mere præcist med årstal, så man f.eks. kan se hvad der er hip nutildags med måneder osv. 
Det samme gælder for genrer, hvis man kunne filtrere noget lidt nyere, siden alt der er højt rated også er gammelt. 
Føles lidt som robotsprog, kunne godt være simplificeret mere eller forklaret mere i dybde. 
Ville være nice hvis der i stedet for “recommended” ville stå noget som f.eks: “Brugere som dig kan godt lide:”.

### Fixes done after user review 
From this feedback we have made some changes to our frontend prototype in Streamlit, made it easier for the user to navigate and learn. We made the following changes:  
- More readable text next to the diagrams.  
- More text in general.  
- Added the amounts of votes to the movie when recommending through genre.
- Changed some of the language use.
- Added more Diagrams for the user to peruse.

### Hit Ratio  
The Hit Ratio is a measure of the system's ability to recommend items that the user actually interacts with or likes. Had our project ever gone into the real world where we could see which users clicked what recommendations, we would be able to test our recommendation system further by calculating users that click a recommendation over total number of users.

### Precision  
Precision is a measure of the accuracy of the recommended items. It focuses on the proportion of correctly recommended items among all the recommended items. This test would have shown a more precise measure of our recommendation system, as it not only tests if we got one recommendation right, but it tests how many of our recommendation are positive (the user liked/clicked it) in all of the recommended movies. the value is between 0 - 1 and the closer we are to 1 the better. It calculates it by taking true positives over true positives - false positives (recommendation the user did not interact with).

## Results
Our content-based recommendation function, works by recommending highly rated titles of the same genre. After conducting some user reviews we concluded that our users are satisfied with the recommendations albeit sometimes they feel like the movies are a bit old. 
Our collaborative filtering systems works on more than just similar genres, it makes a user similarity matrix and then calculates weighted average ratings from similar users. We decided to use SVD to decompose the user-item matrix used to create the similarity matrix, since SVD handles sparse matrices well and is less sensitive to sparse data, giving us a collaborative filtering system that is more scalable and suffers less from the "cold start" problem.

If this project was scaled up in size, we feel there would be a chance that it could help users get a good movie recommendation without being overwhelmed by the infinite choices the vast internet supplies them with. We also feel like we have created a basic version of a system a streaming company would be able to use to recommend movies to other users based on their user base, thus helping them keep their customers with them, while at the same time being satisfied with the service.  

## Streamlit
To open the Streamlit app open a terminal/console on the Exam folder and type "streamlit run Overview.py".

---

Tobias Carlsen - cph-tc183@cphbusiness.dk

Christian Kortsen - cph-cc283@cphbusiness.dk

Daniel Trelborg - cph-dh216@cphbusiness.dk

Simone Toft Hansen - cph-sh575@cphbusiness.dk
