import pandas as pd 

# Import original .csv
dataSteamDataset = pd.read_csv('SteamGames_Description.csv') 

dataSteamDataset = dataSteamDataset.dropna()

# Quita columna añadida al refinar
dataSteamDataset.pop('Unnamed: 0')

dataSteamDataset.to_csv('SteamGames_Description_wthBlank.csv', sep =',')
print("\nDatasetSteam filtered\n") 

# Representa valor de la fila
#print(dataSteamDataset.iloc[5])

