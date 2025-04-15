import pandas as pd

####################################################
# 1) LOAD ALL CSV FILES
####################################################

# a) Races (for 'raceId' → 'year')
df_races = pd.read_csv("f1_races_2021_2024.csv")

# b) Drivers info (for 'driverId' → 'driverRef')
df_drivers = pd.read_csv("filtered_drivers_2021_2024.csv")

# c) Constructor predictions (not used here, but loaded for completeness)
df_constructor_preds = pd.read_csv("ConstructorPrediction.csv")

# d) Driver standings for all seasons (2021-2024), which do *not* have a 'year' column by default
df_standings_raw = pd.read_csv("filtered_driver_standings_2021_2024.csv")

####################################################
# 2) MERGE STANDINGS WITH RACES TO GET 'year'
####################################################
# Most importantly, we attach the 'year' column to each row in df_standings_raw by merging on 'raceId'
df_standings = pd.merge(
    df_standings_raw,
    df_races[['raceId', 'year']],  # only need raceId and year
    on='raceId',
    how='left'
)

# Now df_standings has columns: raceId, driverId, points, position, (and others) *plus* a year column

####################################################
# 3) IF NEEDED: SELECT FINAL DRIVER STANDINGS PER YEAR
####################################################
# If the CSV is one row per race, we must isolate the final standings of each year.
def get_final_standings_for_year(df, year):
    # Filter to one season
    df_year = df[df['year'] == year].copy()
    # Sort so final race is last
    if 'raceId' in df_year.columns:
        df_year.sort_values(by='raceId', inplace=True)
    # Group by driverId, take the last row => final points/position of the season
    df_final = df_year.groupby('driverId', as_index=False).tail(1)
    return df_final

# Repeat for each season
df_2021 = get_final_standings_for_year(df_standings, 2021)
df_2022 = get_final_standings_for_year(df_standings, 2022)
df_2023 = get_final_standings_for_year(df_standings, 2023)
df_2024 = get_final_standings_for_year(df_standings, 2024)

# Rename columns to reflect each year's points & standings
df_2021.rename(columns={'points': '2021_Points', 'position': '2021_Standings'}, inplace=True)
df_2022.rename(columns={'points': '2022_Points', 'position': '2022_Standings'}, inplace=True)
df_2023.rename(columns={'points': '2023_Points', 'position': '2023_Standings'}, inplace=True)
df_2024.rename(columns={'points': '2024_Points', 'position': '2024_Standings'}, inplace=True)

####################################################
# 4) MERGE EACH YEAR INTO A SINGLE DATAFRAME
####################################################
# We'll do sequential merges on 'driverId' with outer joins 
# so we keep drivers even if they appear in fewer than all 4 years.

df_21_22 = pd.merge(
    df_2021[['driverId', '2021_Points', '2021_Standings']],
    df_2022[['driverId', '2022_Points', '2022_Standings']],
    on='driverId',
    how='outer'
)

df_21_22_23 = pd.merge(
    df_21_22,
    df_2023[['driverId', '2023_Points', '2023_Standings']],
    on='driverId',
    how='outer'
)

df_all_years = pd.merge(
    df_21_22_23,
    df_2024[['driverId', '2024_Points', '2024_Standings']],
    on='driverId',
    how='outer'
)

####################################################
# 5) MERGE IN DRIVER INFO (DRIVERREF)
####################################################
df_merged = pd.merge(
    df_all_years,
    df_drivers[['driverId', 'driverRef']],  # columns we need
    on='driverId',
    how='left'
)

# Now df_merged has columns:
#  driverId, 2021_Points, 2021_Standings, 2022_Points, 2022_Standings, etc.
#  plus driverRef (if found).

####################################################
# 6) ADD EMPTY COLUMNS FOR 2025
####################################################
df_merged['2025_Points'] = ""
df_merged['2025_Standings'] = ""

####################################################
# 7) REORDER COLUMNS & SAVE TO CSV
####################################################
desired_columns = [
    'driverId', 'driverRef',
    '2021_Points', '2021_Standings',
    '2022_Points', '2022_Standings',
    '2023_Points', '2023_Standings',
    '2024_Points', '2024_Standings',
    '2025_Points', '2025_Standings'
]

df_final = df_merged[desired_columns]

df_final.to_csv("DriverPredictions2025.csv", index=False)
print("DriverPredictions2025.csv has been created!")
