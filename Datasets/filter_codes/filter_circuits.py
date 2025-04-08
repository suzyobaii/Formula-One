import pandas as pd

circuits_df = pd.read_csv("Datasets/unfiltered_datasets/circuits.csv")
races_df = pd.read_csv("Datasets/filtered_datasets/f1_races_2021_2024.csv")

filtered_circuit_ids = races_df['circuitId'].unique()
filtered_circuits = circuits_df[circuits_df['circuitId'].isin(filtered_circuit_ids)]


filtered_circuits.to_csv('filtered_circuits_2021_2024.csv', index=False)

print("Filtered circuits (2021–2024) saved to 'filtered_circuits_2021_2024.csv'")