import pandas as pd

races = pd.read_csv("Datasets/unfiltered_datasets/races.csv")
races_2021_2024 = races[(races['year'] >= 2021) & (races['year'] <= 2024)]

print(races_2021_2024)

races_2021_2024.to_csv('f1_races_2021_2024.csv', index=False)

