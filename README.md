# Music_CBF

## Introduction
In this page, we will be looking into **content based filtering (CBF)** for music.
Although the code for this model is not completely accurate or great, 
it does provide a good sense of what CBF is and how to emulate it using Python.
Also, this is an extremely detailed explanation in which I try to show my process for every bit.

## Content Based Filtering
Content Based Filtering is a recommendation system that is widely used among online platforms to provide users with potential products to consume.
Although the details may differ, it basically uses the idea that if a user likes a certain Content A, then they will also like a Content B similar to Content A. 
![Content Based Filtering](https://miro.medium.com/max/792/1*P63ZaFHlssabl34XbJgong.jpeg) 

(Image from: https://miro.medium.com/max/792/1*P63ZaFHlssabl34XbJgong.jpeg)

Like the diagram above, CBF recommender systems use a user's past preferences and ratings to suggest other items of potential interest. In order to do this, however, a computer model will need enough data and training to know which items are similar and which are not. This is where a system for calculating similarity is put into place. Most programs use **cosine similarity**, which calculates the similarity of two vectors. But in this model, I will be using simple arithmetic calculations to find similar songs to a choice of music by the user. Keep in mind that this program is not meant for actual recommendations but is more of a test trial to demonstrate a recommender system and provide a good sense of CBF.

## Dataset
The data for this model is from [this kaggle dataset](https://www.kaggle.com/yamaerenay/spotify-dataset-19212020-160k-tracks).
Specifically, I used the data_o.csv file for this model. It provides information about songs that Spotify, a famous audio streaming service, has looked into. Every song is categorized by multiple topics, such as valence, year, artist, danceability, energy, and more. These will be important factors that will be used to help our model determine which songs are similar. 

This is a small representation of how it looks like on a spreadsheet (the actual data is too big to show here):

| Name | Year | Popularity | Artists |
|---|:---:|:---:|---|
| Dynamite | 2020 | 97 | BTS |
| Dakiti | 2020 | 100 | Bad Bunny, Jhay Cortez |
| High Hopes | 2018 | 84 | Panic! At The Disco |

However, I did not use all the data for this model but just the most popular 11000 songs (those with a popularity score of over 50). This reduced a lot of time and computing power while not affecting the results dramatically since unpopular songs will not be recommended often anyways. I also reduced the number of columns down to just 'name', 'popularity', 'year', and 'artists' because I will not be needing the rest of the data for this specific recommender system.

## Actual Code

### 1. Similarity by Year Difference

First of all, we need to import some python tools that are neccessary such as pandas and numpy. They will help with calculations and organizing data. 
```python
import pandas as pd
import numpy as np
```

Then, we import the music data (which is called 'filtered_data.csv' in my device) using pandas dataframe. We will be naming it df1. 
```python
df1=pd.read_csv('filtered_data.csv')
```

Now, in order to extract data about a given song a compare the feature to other songs, we will be making a new index  that basically has the title of a music as the index and the original index number as the column. Therefore, we can type in a title and receive the index number of a song. (This is all for convenience)
```python
indices = pd.Series(df1.index, index=df1['name']).drop_duplicates() #title to number
```

We will first work on comparing songs using their released year. The method in which this will work is 
1. We extract the year information from our wanted song, 
2. Find the difference between that found year and every other year,
3. Sort out the difference,
4. and Select the most similar songs.

We start off by finding the index (number) of out wanted song. (We will leave the song title as simply 'name' and put it in a function later)
```python
idx=indices.loc[name]
```

Then, we create a list called sim_scores, which will have all the year differences. 
```python
sim_scores=list(enumerate(abs(df1["year"]-df1.loc[idx]['year'])))

abs(df1["year"]-df1.loc[idx]['year'] # This part subtracts the two years and puts an absolute value on them.
```
By enumerating, we are basically making sure that the year difference we calculated still has the index of the original song. For exmaple, if Dynamite (index=2) was to be compared with another song released in 2020, without the enumerate code, only the number 0 will be added to sim_scores. Therefore, we cannot recognize which song is which later on. But by enumerating, (2,0) will be added to sim_scores, which we can later use the former number to find out that the song with a difference of 0 has the index 2, which is Dynamite.

To explain a bit about the code within the enumerate code:
```python
abs(df1["year"]-df1.loc[idx]['year']
```
This is where we basically subtract the year of our wanted song from every row of the column of 'year' in the original dataframe. To visualize, if our song is called "Random Song" released in 2018, we subtract 2018 from every year value from the table below. 

| Index | Year |
|---|---|
|0|2019|
|1|2018|
|2|2017|
|3|2016|

2019-2018=1

2018-2018=0

2017-2018=-1

2016-2018=-2

However, simply saving the difference like this can make the computer think that our "Random Song" is more similar to the 2016 released song than the 2019 released song as the value of -2<1. By using absolute value, we can eliminate this problem.
After going through this process with the abs() function, we can enumerate data like this.

sim_scores =
(index number, year difference)
(0,1)
(1,0)
(2,1)
(3,2)

Now, we just sort out the songs based in the year difference.
```python
sim_scores.sort(key=get_second)
```
You may be confused in why key=get_second is included in there and what it is. Let's first define "get_second".
```python
def get_second(x):
    return x[1]
```
This function will basically get the 2nd value of whatever list we plug in. In our case, it will get you the year differnce of whatever song is within sim_scores since the data is organized like this: (index number, year difference)

Using this as the key, we can sort the list sim_scores by the year difference of every song, not by the index number. After this, we just print out the first ten songs within this sorted list (You could print out more if you wanted to)

```python
sim_scores=sim_scores[1:11] # only the first ten
sim_scores = [i[0] for i in sim_scores] # Since the data is still (index,year difference), we just pull out the index number
for i in sim_scores:
  print(df1.loc[i]['name']) # We finally print out the titles of the ten songs.
```

With all this, let's combine it into one simple function. 

```python
def recom_by_year(name, get_second=get_second):
    indices = pd.Series(df1.index, index=df1['name']).drop_duplicates() 
    idx=indices.loc[name]
    sim_scores=list(enumerate(abs(df1["year"]-df1.loc[idx]['year'])))
    sim_scores.sort(key=get_second)
    sim_scores=sim_scores[1:11]
    sim_scores = [i[0] for i in sim_scores]
    for i in sim_scores:
       print(df1.loc[i]['name'])
```

Testing out this function with 'Dakiti', a song released in 2020 with the index as 0, we get the list:



Mood (feat. iann dior)

Dynamite

WAP (feat. Megan Thee Stallion)

positions

What You Know Bout Love

Blinding Lights

For The Night (feat. Lil Baby & DaBaby)

Holy (feat. Chance The Rapper)

Lonely (with benny blanco)

you broke me first



We get a list full of songs released in 2020. So the year similarity code is working.

### 2. Cosine Similarity

Although I wanted to apply cosine similarity into this set of data for recommendations, the data was not really fit for cosine similarity. 
However, using cosine similarity is not that hard to explain: Just use the same code as I did but plug in cosine similarity where we calculate the year difference!
To explain further, cosine similarity is a measuring system which calculates the angle difference between two vectors, which becomes the similarity score. The actual equation for this is:

![Cosine Similarity](https://neo4j.com/docs/graph-data-science/current/_images/cosine-similarity.png) 

(Image from: https://neo4j.com/docs/graph-data-science/current/_images/cosine-similarity.png)

However, we can eliminate this complicated process in our code since we can just import scikit learn, a python tool that helps with these kind of situations. 
Then, we can import cosine simiarity, a tool within scikit learn.
After that, in the same code that I just provided, just change the absolute value year difference code with cosine similarity.

This is the code for this process (not included in the Music_Recommendation.py document):


```python
import sklearn.metrics.pairwise
from sklearn.metrics.pairwise import cosine_similarity
```
Import the code



```python
def get_cosine_sim(v1,v2):
    pop1=np.array([v1])
    pop2=np.array([v2])
    pop2=pop2.reshape(-1,1)
    return sklearn.metrics.pairwise.cosine_similarity(pop1, pop2, dense_output=True)
```
Define cosine simialrity


```python
def cosine_sim_recom(name, get_cosine_sim=get_cosine_sim, get_second=get_second):
    indices = pd.Series(df1.index, index=df1['name']).drop_duplicates() 
    idx=indices.loc[name]
    sim_scores=list(enumerate(get_cosine_sim(df1['popularity'], df1.loc[idx]['popularity'])))
    sim_scores.sort(key=get_second)
    sim_scores=sim_scores[-11:-1]
    sim_scores = [i[0] for i in sim_scores]
    for i in sim_scores:
       print(df1.loc[i]['name'])
```
Plug in cosine similarity


As I have stated before, the dataset was not really fit for cosine similarity, so I don't know if this will work. But hopefully it provides a good enough explanation as to what cosine similarity is and how to use it for recommender systems.





Thank you for reading!
