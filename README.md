# Music_CBF

## Introduction
In this page, we will be looking into **content based filtering (CBF)** for music.
Although the code for this model is not completely accurate or finished, 
it does provide a good sense of what CBF is and how to emulate it using Python Code.

## Content Based Filtering
Content Based Filtering is a recommendation system that is widely used among online platforms to provide users with potential products to consume.
Although the details may differ, it basically uses the idea that if a user likes a certain Content A, then they will also like a Content B similar to Content A. 
![Content Based Filtering](https://miro.medium.com/max/792/1*P63ZaFHlssabl34XbJgong.jpeg) 

(Image from: https://miro.medium.com/max/792/1*P63ZaFHlssabl34XbJgong.jpeg)

Like the diagram above, CBF recommender systems use a user's past preferences and ratings to suggest other items of potential interest. In order to do this, however, a computer model will need enough data and training to know which items are similar and which are not. This is where a system for calculating similarity is put into place. Most programs use cosine similarity, which calculates the similarity of two vectors. In this model, I will be using cosine similarity as well as simple arithmetic calculations to find similar songs to a choice of music by the user. Keep in mind that this program is not meant for actual recommendations but is more of a test trial to set up the basis of a much better recommender system.

## Dataset
The data for this model is from [this kaggle dataset](https://www.kaggle.com/yamaerenay/spotify-dataset-19212020-160k-tracks).
Specifically, I used the data_o.csv file for this model. It provides information about songs that Spotify, a famous audio streaming service, has looked into. Every song is categorized by multiple topics, such as valence, year, artist, danceability, energy, and more. These will be important factors that will be used to help our model determine which songs are similar. 

This is a small representation of how it looks like on a spreadsheet (the actual data is too big to show here):

| Title | Year | Popularity | Artists |
|---|:---:|:---:|---|
| Dynamite | 2020 | 97 | BTS |
| Dakiti | 2020 | 100 | Bad Bunny, Jhay Cortez |
| High Hopes | 2018 | 84 | Panic! At The Disco |

## Actual Code

