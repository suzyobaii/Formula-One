from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    driver_data = pd.read_csv("DriverPredictions2025_withForecast.csv")
    constructor_data = pd.read_csv("ConstructorPrediction_withForecast.csv")

    driver_html = driver_data.to_html(classes='table table-bordered', index=False)
    constructor_html = constructor_data.to_html(classes='table table-bordered', index=False)

    return render_template('index.html', driver_html=driver_html, constructor_html=constructor_html)

if __name__ == '__main__':
    app.run(debug=True)
