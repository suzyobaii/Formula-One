import pandas as pd

# 1. Load the data
df_races = pd.read_csv("f1_races_2021_2024.csv")
df_const_standings = pd.read_csv("filtered_constructor_standings_2021_2024.csv")
df_constructors = pd.read_csv("filtered_constructors_2021_2024.csv")

# 2. Merge constructor standings with race data to access the 'year' column
#    We only need 'raceId' and 'year' from the races DataFrame
df_merged = pd.merge(
    df_const_standings,
    df_races[['raceId', 'year']],
    on='raceId',
    how='left'
)

# 3. Merge in the constructor name
#    (Assuming df_constructors has columns 'constructorId' and 'name')
df_merged = pd.merge(
    df_merged,
    df_constructors[['constructorId', 'name']],
    on='constructorId',
    how='left'
)

# 4. Filter for 2021 data
df_2021 = df_merged[df_merged['year'] == 2021].copy()

# 5. (Optional) If you only want the final standings (the last race in 2021) for each constructor:
#    Sort by 'raceId' (ascending) and use groupby().tail(1)
df_2021_final = (
    df_2021.sort_values(by='raceId')
           .groupby('constructorId', as_index=False)
           .tail(1)
)

# 6. Select the columns you need
df_filtered = df_2021_final[['name', 'points', 'position', 'wins']].copy()

# 7. Rename 'name' -> 'constructor'
df_filtered.rename(columns={'name': 'constructor'}, inplace=True)

# 8. Write the filtered DataFrame to a CSV file
df_filtered.to_csv("2021_constructor_standings.csv", index=False)

print("Filtered 2021 constructor data has been saved to '2021_constructor_standings.csv'.")
