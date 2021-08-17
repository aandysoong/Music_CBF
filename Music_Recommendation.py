# import pandas and the data
import pandas as pd
df1=pd.read_csv('filtered_data.csv') # save into a dataframe

# function for later use
def get_second(x):
    return x[1]

# actual function 
def recom_by_year(name, get_second=get_second):
    indices = pd.Series(df1.index, index=df1['name']).drop_duplicates() # convert title to index
    idx=indices.loc[name] # find the index of the song
    sim_scores=list(enumerate(abs(df1["year"]-df1.loc[idx]['year']))) # calculate the year difference
    sim_scores.sort(key=get_second) 
    sim_scores=sim_scores[1:11]
    sim_scores = [i[0] for i in sim_scores]
    for i in sim_scores: # print out the songs
       print(df1.loc[i]['name'])

recom_by_year('Dakiti')