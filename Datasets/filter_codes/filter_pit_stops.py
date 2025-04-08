import pandas as pd

results_df = pd.read_csv('Datasets/filtered_datasets/filtered_results_2021_2024.csv')

ps_df = pd.read_csv('Datasets/unfiltered_datasets/pit_stops.csv')

ps_ids = results_df['raceId'].unique()

filtered_drivers = ps_df[ps_df['raceId'].isin(ps_ids)]

filtered_drivers.to_csv('filtered_pit_stops_2021_2024.csv', index=False)

print("Filtered drivers data for 2021 to 2024 has been saved to 'filtered_pit_stops_2021_2024.csv'.")