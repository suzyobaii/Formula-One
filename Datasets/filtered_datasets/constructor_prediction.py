import pandas as pd
from sklearn.ensemble import RandomForestRegressor

df = pd.read_csv("ConstructorPrediction.csv")
df_model = df.dropna(subset=[
    '2021_Points', '2022_Points', '2023_Points', '2024_Points'
])

X = df_model[['2021_Points', '2022_Points', '2023_Points', '2024_Points']]
y = df_model['2024_Points']

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X, y)

X_all = df[['2021_Points', '2022_Points', '2023_Points', '2024_Points']].fillna(0)
df['Predicted_2025_Points'] = model.predict(X_all).round(1)
df['Predicted_2025_Standings'] = df['Predicted_2025_Points'].rank(ascending=False, method='min').astype(int)
df.to_csv("ConstructorPrediction_withForecast.csv", index=False)
print("Constructor forecast complete! Output saved to ConstructorPrediction_withForecast.csv")
