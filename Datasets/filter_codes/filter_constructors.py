import pandas as pd
results_df = pd.read_csv('Formula-One/Datasets/filtered_datasets/filtered_results_2021_2024.csv')

c_df = pd.read_csv('Formula-One/Datasets/unfiltered_datasets/constructors.csv')

c_ids = results_df['constructorId'].unique()

filtered_drivers = c_df[c_df['constructorId'].isin(c_ids)]

filtered_drivers.to_csv('filtered_constructors_2021_2024.csv', index=False)

print("Filtered drivers data for 2021 to 2024 has been saved to 'filtered_constructors_2021_2024.csv'.")