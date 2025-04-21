import pandas as pd

df_races = pd.read_csv("f1_races_2021_2024.csv")
df_const_standings = pd.read_csv("filtered_constructor_standings_2021_2024.csv")
df_constructors = pd.read_csv("filtered_constructors_2021_2024.csv")


df_merged = pd.merge(
    df_const_standings,
    df_races[['raceId', 'year']],
    on='raceId',
    how='left'
)


df_merged = pd.merge(
    df_merged,
    df_constructors[['constructorId', 'name']],
    on='constructorId',
    how='left'
)

df_2024 = df_merged[df_merged['year'] == 2024].copy()

df_2024_final = (
    df_2024.sort_values(by='raceId')
           .groupby('constructorId', as_index=False)
           .tail(1)
)

df_filtered = df_2024_final[['name', 'points', 'position', 'wins']].copy()

df_filtered.rename(columns={'name': 'constructor'}, inplace=True)

df_filtered.to_csv("2024_constructor_standings.csv", index=False)

print("Filtered 2024 constructor data has been saved to '2024_constructor_standings.csv'.")
