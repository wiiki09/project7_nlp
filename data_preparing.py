import json
from pprint import pprint
import pandas as pd

with open('./data/case_data.json') as f:
    data = json.load(f)

#pprint(data)

Descriptions=[] # a list contains all the description, note each discription may have more than 1 sentence
Functions=[]   #these are our labels

all_data=data['data']
#note: the data['data'] key is a list of dictionaries, we need to extract the value of decription and function
for d in all_data:
    Descriptions.append(d.get('description'))
    Functions.append(d.get('function'))

print(len(Functions))
print(len(Descriptions))
print(Descriptions[0])
print(Functions[0])


#create a csv file that we will use it later in colab
#store the csv in the data folder

#1. create a dictionary
data_to_model= {"Descriptions":Descriptions,  "Functions":Functions}
# 2. create a df
df=pd.DataFrame(data_to_model)
#3. create a csv file
df.to_csv("./data/data_to_model.csv")

