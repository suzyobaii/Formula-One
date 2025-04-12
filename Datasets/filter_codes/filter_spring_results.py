import pandas as pd
results_df = pd.read_csv('Formula-One/Datasets/filtered_datasets/filtered_results_2021_2024.csv')

sr_df = pd.read_csv('Formula-One/Datasets/unfiltered_datasets/sprint_results.csv')

sr_ids = results_df['raceId'].unique()

filtered_drivers = sr_df[sr_df['raceId'].isin(sr_ids)]

filtered_drivers.to_csv('filtered_sprint_results_2021_2024.csv', index=False)

print("Filtered drivers data for 2021 to 2024 has been saved to 'filtered_sprint_results_2021_2024.csv'.")