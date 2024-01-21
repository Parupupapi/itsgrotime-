from flask import Flask, render_template, request
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

app = Flask(__name__)

# Load the weather data
data = pd.read_csv('/Users/anisiva/Documents/Github/LastTry/linear regression project/weather_data.csv')

# Prepare the data for training
x = data.drop(['Rating', 'Date'], axis=1).values
y = data['Rating'].values

# Train the Linear Regression model
ml = LinearRegression()
ml.fit(x, y)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate_rating', methods=['POST'])
def calculate_rating():
    plantname = request.form['plantname']
    idealtemp = request.form['idealtemp']
    idealhumidity = request.form['idealhumidity']
    idealsunlight = request.form['idealsunlight']

    rating_output = ml.predict([[int(idealtemp), int(idealtemp), int(idealhumidity), int(idealsunlight)]])
    rating_output = round(rating_output[0], 2)

    return render_template('result.html', plantname=plantname, output=rating_output)

@app.route('/forecast_today', methods=['POST'])
def forecast_today():
    todaytemphigh = request.form['todaytemphigh']
    todaytemplow = request.form['todaytemplow']
    todayhumidity = request.form['todayhumidity']
    todaysunlight = request.form['todaysunlight']

    todayoutput = ml.predict([[int(todaytemphigh), int(todaytemplow), int(todayhumidity), int(todaysunlight)]])
    todayoutput = round(todayoutput[0], 2)

    rating_output = float(request.form['output'])
    difference = abs(rating_output - todayoutput)

    if difference < 10:
        prompt = "You can plant the plant today. Conditions are suitable."
    elif 10 <= difference < 20:
        prompt = "Consider planting the plant with caution. Conditions are moderately suitable."
    else:
        prompt = "It's not recommended to plant the plant today. Conditions are not suitable."

    return render_template('forecast_result.html', todaysoutput=todayoutput, difference=difference, prompt=prompt)

@app.route('/compare_ratings', methods=['POST'])
def compare_ratings():
    plantname = request.form['plantname']
    todaytemphigh = request.form['todaytemphigh']
    todaytemplow = request.form['todaytemplow']
    todayhumidity = request.form['todayhumidity']
    todaysunlight = request.form['todaysunlight']

    rating_output = ml.predict([[int(todaytemphigh), int(todaytemplow), int(todayhumidity), int(todaysunlight)]])
    rating_output = round(rating_output[0], 2)

    output = float(request.form.get('output', 0))

    difference = abs(output - rating_output)

    if difference < 10:
        prompt = "You can plant the plant today. Conditions are suitable."
    elif 10 <= difference < 20:
        prompt = "Consider planting the plant with caution. Conditions are moderately suitable."
    else:
        prompt = "It's not recommended to plant the plant today. Conditions are not suitable."

    return render_template('compare_ratings.html', plantname=plantname, prompt=prompt)

if __name__ == '__main__':
    app.run(debug=True)
