import pandas as pd



df_races = pd.read_csv("f1_races_2021_2024.csv")
df_drivers = pd.read_csv("filtered_drivers_2021_2024.csv")
df_constructor_preds = pd.read_csv("ConstructorPrediction.csv")
df_standings_raw = pd.read_csv("filtered_driver_standings_2021_2024.csv")

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

selected_driver_ids = [
    1, 4, 807, 815, 817, 822, 825, 830, 832, 839, 840, 842,
    844, 846, 847, 848, 852, 855, 857, 858, 859, 860, 861, 862
]

df_final = df_final[df_final['driverId'].isin(selected_driver_ids)]
df_final.to_csv("DriverPredictions2025.csv", index=False)
print("DriverPredictions2025.csv has been created!")
