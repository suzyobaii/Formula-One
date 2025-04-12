import pandas as pd
results_df = pd.read_csv('Formula-One/Datasets/filtered_datasets/f1_races_2021_2024.csv')

q_df = pd.read_csv('Formula-One/Datasets/unfiltered_datasets/seasons.csv')

q_ids = results_df['year'].unique()

filtered_drivers = q_df[q_df['year'].isin(q_ids)]

filtered_drivers.to_csv('filtered_seasons_2021_2024.csv', index=False)

print("Filtered drivers data for 2021 to 2024 has been saved to 'filtered_seasons_2021_2024.csv'.")