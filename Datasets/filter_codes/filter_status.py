import pandas as pd

results_df = pd.read_csv('filtered_datasets/filtered_results_2021_2024.csv')

lt_df = pd.read_csv('unfiltered_datasets/status.csv')

lt_ids = results_df['statusId'].unique()



filtered_drivers = lt_df[lt_df['statusId'].isin(lt_ids)]

filtered_drivers.to_csv('filtered_status_2021_2024.csv', index=False)

print("Filtered drivers data for 2021 to 2024 has been saved to 'filtered_status_2021_2024.csv'.")