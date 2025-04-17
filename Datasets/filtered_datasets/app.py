from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    # Read the data from your CSV file
    data = pd.read_csv("DriverPredictions2025.csv")  # Your uploaded CSV file
    # Convert data to HTML table format
    data_html = data.to_html(classes='table table-bordered', index=False)
    return render_template('index.html', data_html=data_html)

if __name__ == '__main__':
    app.run(debug=True)
