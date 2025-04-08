import pandas as pd


results_df = pd.read_csv('Datasets/unfiltered_datasets/results.csv')
races_df = pd.read_csv("Datasets/filtered_datasets/f1_races_2021_2024.csv")


filtered_results_ids = races_df['raceId'].unique()
filtered_results = results_df[results_df['raceId'].isin(filtered_results_ids)]


filtered_results.to_csv('filtered_results_2021_2024.csv', index=False)
print("Filtered results (2021–2024) saved to 'filtered_results_2021_2024.csv'")