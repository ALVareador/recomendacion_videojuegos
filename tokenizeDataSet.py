from nltk.tokenize import word_tokenize 
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

import nltk
import pandas as pd

# pip install nltk
# nltk.download('punkt')
# nltk.download('stopwords')

dataSteamDataset = pd.read_csv('SteamGames_Description_wthBlank.csv') 

ps = PorterStemmer()

preprocessedText = []

for row in dataSteamDataset.itertuples():
    
    
    text = word_tokenize(row[3]) ## indice de la columna que contiene el texto, en este caso game_description
    ## Remove stop words
    stops = set(stopwords.words("english"))
    text = [ps.stem(w) for w in text if not w in stops and w.isalnum()]
    text = " ".join(text)
    
    preprocessedText.append(text)

preprocessedData = dataSteamDataset
preprocessedData['processed_text'] = preprocessedText

for row in dataSteamDataset.itertuples():
    
    
    text = word_tokenize(row[11]) ## indice de la columna que contiene el texto, en este caso steampy_tags
    ## Remove stop words
    stops = set(stopwords.words("english"))
    text = [ps.stem(w) for w in text if not w in stops and w.isalnum()]
    text = " ".join(text)
    
    preprocessedText.append(text)

preprocessedData = dataSteamDataset
preprocessedData['processed_tags'] = preprocessedText

preprocessedData.pop('Unnamed: 0')

#Para el notebook liminar estas 2 lineas y substituir por preprocessedData a secas para que lo muestre
preprocessedData.to_csv('SteamGames_Description_Tokenized.csv', sep =',')

print('DataSet tokenized')
