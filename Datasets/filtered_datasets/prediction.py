import pandas as pd
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import numpy as np

df = pd.read_csv("DriverPredictions2025.csv")
df_model = df.dropna(subset=[
    '2021_Points', '2022_Points', '2023_Points', '2024_Points'
])

X = df_model[['2021_Points', '2022_Points', '2023_Points', '2024_Points']]
y = df_model['2024_Points']  

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X, y)

X_all = df[['2021_Points', '2022_Points', '2023_Points', '2024_Points']].fillna(0)

df['2025_Points'] = model.predict(X_all).round(1)

df['2025_Standings'] = df['2025_Points'].rank(ascending=False, method='min').astype(int)

final_df = df[[
    'driverId', 'driverRef',
    '2021_Points', '2021_Standings',
    '2022_Points', '2022_Standings',
    '2023_Points', '2023_Standings',
    '2024_Points', '2024_Standings',
    '2025_Points', '2025_Standings'
]]

final_df.to_csv("DriverPredictions2025_withForecast.csv", index=False)
print("Prediction complete! Output saved to DriverPredictions2025_withForecast.csv")
