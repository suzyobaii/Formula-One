import pandas as pd

results_df = pd.read_csv('Datasets/filtered_datasets/filtered_results_2021_2024.csv')

lt_df = pd.read_csv('Datasets/unfiltered_datasets/lap_times.csv')

lt_ids = results_df['raceId'].unique()

filtered_drivers = lt_df[lt_df['raceId'].isin(lt_ids)]

filtered_drivers.to_csv('filtered_lap_times_2021_2024.csv', index=False)

print("Filtered drivers data for 2021 to 2024 has been saved to 'filtered_lap_times_2021_2024.csv'.")