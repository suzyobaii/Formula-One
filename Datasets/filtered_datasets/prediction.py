import pandas as pd

df_races = pd.read_csv("datasets/filtered_datasets/f1_races_2021_2024.csv")
df_drivers = pd.read_csv("datasets/filtered_datasets/filtered_drivers_2021_2024.csv")
df_constructor_preds = pd.read_csv("datasets/filtered_datasets/ConstructorPrediction.csv")
df_standings_raw = pd.read_csv("datasets/filtered_datasets/filtered_driver_standings_2021_2024.csv")

df_standings = pd.merge(
    df_standings_raw,
    df_races[['raceId', 'year']],  
    on='raceId',
    how='left'
)

def get_final_standings_for_year(df, year):
    df_year = df[df['year'] == year].copy()
    if 'raceId' in df_year.columns:
        df_year.sort_values(by='raceId', inplace=True)
    df_final = df_year.groupby('driverId', as_index=False).tail(1)
    return df_final

df_2021 = get_final_standings_for_year(df_standings, 2021)
df_2022 = get_final_standings_for_year(df_standings, 2022)
df_2023 = get_final_standings_for_year(df_standings, 2023)
df_2024 = get_final_standings_for_year(df_standings, 2024)

df_2021.rename(columns={'points': '2021_Points', 'position': '2021_Standings'}, inplace=True)
df_2022.rename(columns={'points': '2022_Points', 'position': '2022_Standings'}, inplace=True)
df_2023.rename(columns={'points': '2023_Points', 'position': '2023_Standings'}, inplace=True)
df_2024.rename(columns={'points': '2024_Points', 'position': '2024_Standings'}, inplace=True)


df_21_22 = pd.merge(
    df_2021[['driverId', '2021_Points', '2021_Standings']],
    df_2022[['driverId', '2022_Points', '2022_Standings']],
    on='driverId',
    how='outer'
)

df_21_22_23 = pd.merge(
    df_21_22,
    df_2023[['driverId', '2023_Points', '2023_Standings']],
    on='driverId',
    how='outer'
)

df_all_years = pd.merge(
    df_21_22_23,
    df_2024[['driverId', '2024_Points', '2024_Standings']],
    on='driverId',
    how='outer'
)


df_merged = pd.merge(
    df_all_years,
    df_drivers[['driverId', 'driverRef']], 
    on='driverId',
    how='left'
)

df_merged['2025_Points'] = ""
df_merged['2025_Standings'] = ""

desired_columns = [
    'driverId', 'driverRef',
    '2021_Points', '2021_Standings',
    '2022_Points', '2022_Standings',
    '2023_Points', '2023_Standings',
    '2024_Points', '2024_Standings',
    '2025_Points', '2025_Standings'
]

df_final = df_merged[desired_columns]

df_final.to_csv("DriverPredictions2025.csv", index=False)
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import numpy as np

df = pd.read_csv("datasets/filtered_datasets/DriverPredictions2025.csv")

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

final_df.to_csv("datasets/filtered_datasets/DriverPredictions2025_withForecast.csv", index=False)
print("Prediction complete! Output saved to DriverPredictions2025_withForecast.csv")

print("DriverPredictions2025.csv has been created!")