import pandas as pd
import requests
import json
import io
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split

ideal_plant_temp = {'Lettuce':62.5, 'Lemon Grass':80,'Tulsi Basil':75}
ideal_plant_humidity = {'Lettuce':60, 'Lemon Grass':55,'Tulsi Basil':50}
ideal_plant_sunlight = {'Lettuce':4, 'Lemon Grass':5,'Tulsi Basil':7}

raw_content_url = 'https://raw.githubusercontent.com/JaCARYK/Weather-Application_baht/main/linear%20regression/weather_data.csv'


# Download the raw content
response = requests.get(raw_content_url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Read CSV from response text
    data = pd.read_csv(io.StringIO(response.text))

    # Now you can use the 'data' DataFrame for further analysis
    #print(data.head())
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")

x = data.drop(['Rating','Date'],axis=1).values
y = data['Rating'].values

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=0)

ml=LinearRegression()
ml.fit(x_train,y_train)



Ideal_Lettuce_Score = ml.predict([[65,60,60,4]])
Ideal_LemonGrass_Score= ml.predict([[85,75,55,5]])
Ideal_TulsiBasil_Score= ml.predict([[80,70,50,7]])

scores_dict = {
    'Lettuce': Ideal_Lettuce_Score[0],
    'Lemon Grass': Ideal_LemonGrass_Score[0],
    'Tulsi Basil': Ideal_TulsiBasil_Score[0],
    # Add scores for other plant types
}


ml.predict([[85,75,80,10]])
one=int(ml.predict([[58,52,90,1]]))
two=ml.predict([[60,48,87,2]])
three=ml.predict([[61,50,83,5]])
four=ml.predict([[56,50,90,2]])
five=ml.predict([[62,50,88,1]])
six=ml.predict([[64,50,78,2]])
sevin=ml.predict([[68,49,68,1]])
eight=ml.predict([[71,50,66,4]])
Nine=ml.predict([[69,49,68,6]])
ten=ml.predict([[70,49,75,2]])

class final_percent:
    def __init__(self, temp_percent):
        self.temp_percent=int(temp_percent)
    def score(self):
        return (Ideal_Lettuce_Score/self.temp_percent), (Ideal_LemonGrass_Score/self.temp_percent), (Ideal_TulsiBasil_Score/self.temp_percent)
result=final_percent(one)
print(result.score())


