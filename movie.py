import pandas as pd
import numpy as np
df1=pd.read_csv('filtered_data.csv')
# print(df1)
def year_sim(year1,year2):
    return abs(year1-year2)

def get_second(x):
    return x[1]

def recom_by_year(name, year_sim=year_sim, get_second=get_second):
    indices = pd.Series(df1.index, index=df1['name']).drop_duplicates() #title to number
    idx=indices.loc[name]
    sim_scores=list(enumerate(abs(df1["year"]-df1.loc[idx]['year'])))
    sim_scores.sort(key=get_second)
    sim_scores=sim_scores[1:11]
    music_indices = [i[0] for i in sim_scores]
    final_list=[]
    for i in music_indices:
        final_list.append(df1.loc[i]['name'])
    return final_list

def print_well(song, recom_by_year=recom_by_year):
    for i in recom_by_year(song):
        print(i)

print_well('Dakiti')