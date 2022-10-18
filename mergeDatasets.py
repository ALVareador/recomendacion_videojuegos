# Need to download wheel ans pandas:
# pip install wheel
# pip install pandas
import pandas as pd 

# Import original .csv
dataSteamDataset = pd.read_csv('steam_original.csv') 
dataSteamGamesDataset= pd.read_csv('steam_games_original.csv')

# pop(name) delete the column 'name' on the .csv
dataSteamDataset.pop('appid')
dataSteamDataset.pop('english')
dataSteamDataset.pop('negative_ratings')
dataSteamDataset.pop('median_playtime')
dataSteamDataset.pop('owners') 

# Add game description to original dataset, pk= 'name'
dataSteamwithDescription = pd.merge(dataSteamGamesDataset.loc[:, ['name','game_description']],dataSteamDataset, on='name', how='outer') 

print("\nDatasetSteam with Description generated\n") 

# Save on SteamGames_Description.csv , Separator: ,
dataSteamwithDescription.to_csv('SteamGames_Description.csv', sep =',')
