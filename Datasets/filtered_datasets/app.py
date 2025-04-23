from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def homepage():
    driver_data = pd.read_csv("DriverPredictions2025_withForecast.csv")
    constructor_data = pd.read_csv("ConstructorPrediction_withForecast.csv")

    driver_html = driver_data.to_html(classes='table table-bordered', index=False)
    constructor_html = constructor_data.to_html(classes='table table-bordered', index=False)

    return render_template('homepage.html', driver_html=driver_html, constructor_html=constructor_html)

@app.route('/teams')
def teams():
    return render_template('teams.html')

@app.route('/cars')
def cars():
    return render_template('cars.html')

@app.route('/tracks')
def tracks():
    return render_template('tracks.html')

@app.route('/predictor')
def predictor():
    driver_data = pd.read_csv("DriverPredictions2025_withForecast.csv")
    constructor_data = pd.read_csv("ConstructorPrediction_withForecast.csv")

    driver_html = driver_data.to_html(classes='table table-bordered', index=False)
    constructor_html = constructor_data.to_html(classes='table table-bordered', index=False)

    return render_template('predictor.html', driver_html=driver_html, constructor_html=constructor_html)

if __name__ == '__main__':
    app.run(debug=True)
