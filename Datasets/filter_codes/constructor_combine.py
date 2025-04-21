import pandas as pd

df_2021 = pd.read_csv("2021_constructor_standings.csv")
df_2022 = pd.read_csv("2022_constructor_standings.csv")
df_2023 = pd.read_csv("2023_constructor_standings.csv")
df_2024 = pd.read_csv("2024_constructor_standings.csv")

df_2021 = df_2021[['constructor', 'points']].rename(columns={'points': '2021_Points'})
df_2022 = df_2022[['constructor', 'points']].rename(columns={'points': '2022_Points'})
df_2023 = df_2023[['constructor', 'points']].rename(columns={'points': '2023_Points'})
df_2024 = df_2024[['constructor', 'points']].rename(columns={'points': '2024_Points'})

df_all = pd.merge(df_2021, df_2022, on='constructor', how='outer')
df_all = pd.merge(df_all, df_2023, on='constructor', how='outer')
df_all = pd.merge(df_all, df_2024, on='constructor', how='outer')

df_all['Predicted_2025_Points'] = ""

df_all.to_csv("ConstructorPrediction.csv", index=False)
print("Combined CSV created: ConstructorPrediction.csv")
