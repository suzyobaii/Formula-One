import pandas as pd
results_df = pd.read_csv('Formula-One/Datasets/filtered_datasets/filtered_results_2021_2024.csv')

c_df = pd.read_csv('Formula-One/Datasets/unfiltered_datasets/constructor_standings.csv')

c_ids = results_df['raceId'].unique()

filtered_drivers = c_df[c_df['raceId'].isin(c_ids)]

filtered_drivers.to_csv('filtered_constructor_standings_2021_2024.csv', index=False)

print("Filtered drivers data for 2021 to 2024 has been saved to 'filtered_constructor_standings_2021_2024.csv'.")