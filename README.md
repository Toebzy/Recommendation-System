# Recommendation-System - BI Exam Project 
![2022_01_Untitled-design-16](https://github.com/Toebzy/Recommendation-System/assets/113095884/6880aebb-c750-4aaa-b0e3-d16b21d94ce4)

## Problem Formulation

In today’s digital era, users are presented with vast amounts of content and choices across various online sites. Using machine learning, we can create a system that helps customers discover relevant content, by providing individualized recommendations. This way, we help the user avoid information overload, which in turn helps create sales and increases company profits.

## Choices 
We had some issues when it came to forming a recommendation. The problem was due to the size of our dataset. Many of the movies had very few or only 1 review. 
This made it difficult to make an average rating for recommendation. We found several larger datasets, but so large that it brought technical issues. 
We decided to use the upper 10th quantile of total votes. This let us have 900+ movies with a minimum of 27 votes. 

## Theoretical Foundation
We needed to decide what to recommend the user, based on existing user data. Based on our dataset, we decided on the WAR (weighted average rating) movie and a genre of your choice. 
However, there is no defenitive way to recommend movies perfectly. Users might like something more than highly rated movies, since critics and user reviews often dont share the same views on entertainment. 
We therefore decidet to developed a more advanced algorithm, that takes a users similarities and recommends movies based on simalar users ratings. This should give more accuruate recommendations based on the previous theory. 

## User Research
### User 1
Noget der checker om de har rettighederne til de film der bliver anbefalet
Han synes det var forståeligt og ligetil.
Han synes der burde være noget i forhold til popularitet, siden en høj rating ikke altid er særligt underholdende. Godfather med høj rating i sort hvid er svær at anbefale ud fra baseret på rating og genre. 
Kunne nemt forstå dataen der blev vist.

### User 2
Forklaring på siderne, siden han har glemt det efter diagrammerne er loadet. Mere tekst ud fra diagrammerne der forklarer hvad han kigger på og hvad det er baseret ud fra. 
Kan laves lidt pænere at kigge på, hvis der er fokus på det.
I stedet for “recommended”, så “recommended to this user”. Igen kan det forklares og vises lidt mere tydeligt hvis man ikke har en der kan forklare hvad ting betyder. 
“It does what I think it would do, straightforward”.

### User 3
Diagram texten er svær at læse, siden det står lodret. Ville være rart hvis det var vinklet. 
Det er nemt og overskueligt at læse. Det kunne være rart at vide hvor mange ratings gennemsnittet er baseret på. Det kunne være rart at kunne være mere præcist med årstal, så man f.eks. kan se hvad der er hip nutildags med måneder osv. 
Det samme gælder for genrer, hvis man kunne filtrere noget lidt nyere, siden alt der er højt rated også er gammelt. 
Føles lidt som robotsprog, kunne godt være simplificeret mere eller forklaret mere i dybde. 
Ville være nice hvis der i stedet for “recommended” ville stå noget som f.ek.s: “Brugere som dig kan godt lide:” 

Ud fra denne feedback har vi lavet opdateringer til vores frontend, og gjort det mere tydeligt for brugeren i form af visualisering. 
From this feedback we have made some changes to our frontend prototype in streamlt, made it easier for the user to navigate and learn we made the following changes:  
- More readable text next to the diagrams
- More text in genreal
- Med mere

## Results
Our user recommendation function, works by recommending highly rated titles of the same genre. We can't get anything meaningful out of this, due to our inability to test it with user surveys. 
The other recomendation system is more advanced, and works on more than just similar genres. Therefore we can also value the response with an accuracy. 
## Streamlit
To open the Streamlit app open a terminal/console on the Exam folder and type "streamlit run Overview.py"

#

Tobias Carlsen - cph-tc183@cphbusiness.dk

Christian Kortsen - cph-cc283@cphbusiness.dk

Daniel Trelborg - cph-dh216@cphbusiness.dk

Simone Toft Hansen - cph-sh575@cphbusiness.dk
