import pandas as pd

results_df = pd.read_csv('Datasets/filtered_datasets/filtered_results_2021_2024.csv')

drivers_df = pd.read_csv('Datasets/unfiltered_datasets/driver_standings.csv')

driver_ids = results_df['raceId'].unique()

filtered_drivers = drivers_df[drivers_df['raceId'].isin(driver_ids)]

filtered_drivers.to_csv('filtered_driver_standings_2021_2024.csv', index=False)

print("Filtered drivers data for 2021 to 2024 has been saved to 'filtered_drivers_2021_2024.csv'.")