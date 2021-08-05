import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics.pairwise import linear_kernel
df1=pd.read_csv('filtered_data.csv')

def get_cosine_sim(v1,v2):
    pop1=np.array([v1])
    pop2=np.array([v2])
    pop1=pop1.reshape(-1,1)
    print(pop2)
    pop2=pop2.reshape(-1,1)
    return linear_kernel(pop1,pop2)

#[원하는 값, 원하는값, ...] * [모든 popularity]

def get_second(x):
    return x[1]

indices = pd.Series(df1.index, index=df1['name']).drop_duplicates() #title to number
idx=indices.loc['Dynamite']
pop_list=[]
df1.loc[idx]['year']
df1.loc[idx]['popularity']
for i in indices:
    pop_list.append(df1.loc[i]['popularity'])

wanted_pop_list=[df1.loc[idx]['popularity']]*11204
#for i in range(0,len(df1)-1):
#    wanted_pop_list.append(df1.loc[idx]['popularity'])
print(wanted_pop_list)
print(pop_list[0].shape)
print(get_cosine_sim(wanted_pop_list, pop_list))

    #print(get_cosine_sim(df1.loc[idx]['popularity'], df1.loc[i]['popularity']))
    #sim_scores=list(enumerate((get_cosine_sim(df1.loc[idx]['popularity'], df1.loc[i]['popularity']))))
#sim_scores.sort(key=get_second)
#sim_scores=sim_scores[1:11]
#print(sim_scores)

'''def recom_by_year(name, year_sim=year_sim, get_second=get_second):
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
'''