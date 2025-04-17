import pandas as pd
import flask
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Lasso
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler

app = flask.Flask(__name__)

# Load data - Ensure the file paths are correct
data_constructor = pd.read_csv("Datasets/filtered_datasets/DriverPredictions2025.csv")
comparison_df = pd.read_csv("Datasets/filtered_datasets/regression_comparison.csv")

# Prediction function
def predict_points(data):
    # Print to verify if data is loaded correctly
    print("Data loaded for prediction:", data.head())

    # Check if the required columns exist
    required_columns = ["driverRating", "carRating", "constructorStrategy", "2021_Points", "2022_Points", "2023_Points", "2024_Points"]

    X = data[required_columns]
    y = data["2024_Points"]

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Scale data
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    X_scaled = scaler.transform(X)

    # Create and train the model
    model = Lasso(alpha=0.1)
    model.fit(X_train_scaled, y_train)

    # Predict and evaluate
    predictions = model.predict(X_test_scaled)
    mse = mean_squared_error(y_test, predictions)
    print("Mean Squared Error:", mse)

    # Make final predictions for 2025
    predicted_2025_points = model.predict(X_scaled)

    # Add predictions to the data
    data["2025_Points"] = predicted_2025_points
    data["2025_Points"] = data["2025_Points"].round().clip(lower=0)
    data["2025_Points"] = data["2025_Points"].apply(lambda x: 0 if x == -0 else x)

    # Sort by predicted points
    data = data.sort_values(by=["2025_Points"], ascending=False)

    # Check the output to ensure the function is working
    print("Predicted Data:", data[["driverRef", "2021_Points", "2022_Points", "2023_Points", "2024_Points", "2025_Points"]].head())
    
    # Save the predicted data to a CSV file
    data.to_csv("DriverPredictions2025.csv", index=False)
    print("Predicted data saved to 'DriverPredictions2025.csv'")

    return data[["driverRef", "2021_Points", "2022_Points", "2023_Points", "2024_Points", "2025_Points"]]

# Flask route to display data
@app.route('/')
def index():
    # Predict points using your data
    predicted_data = predict_points(data_constructor)

    # Check if data is returned
    if predicted_data is None:
        return "Error: No data to display."

    # Convert to HTML table
    data_html = predicted_data.to_html(classes='table table-bordered', index=False)

    # Render HTML with data
    return flask.render_template('index.html', data_html=data_html)

if __name__ == '__main__':
    app.run(debug=True)