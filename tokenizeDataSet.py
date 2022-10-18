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
preprocessedTags = []

for row in dataSteamDataset.itertuples():
    
    
    text = word_tokenize(row[3]) ## indice de la columna que contiene el texto, en este caso game_description
    ## Remove stop words
    stops = set(stopwords.words("english"))
    text = [ps.stem(w) for w in text if not w in stops and w.isalnum()]
    text = " ".join(text)
    
    preprocessedText.append(text)

preprocessedData = dataSteamDataset
preprocessedData['processed_text'] = preprocessedText

print("processed_text generated")

for row in preprocessedData.itertuples():
    
    
    text = word_tokenize(row[11]) ## indice de la columna que contiene el texto, en este caso tags
    ## Remove stop words
    stops = set(stopwords.words("english"))
    text = [ps.stem(w) for w in text if not w in stops and w.isalnum()]
    text = " ".join(text)
    
    preprocessedTags.append(text)

preprocessedData2 = dataSteamDataset
preprocessedData2['processed_tags'] = preprocessedTags

print("processed_tags generated")

preprocessedData2.pop('Unnamed: 0')

#Para el notebook liminar estas 2 lineas y substituir por preprocessedData a secas para que lo muestre
preprocessedData2.to_csv('SteamGames_Description_Tokenized.csv', sep =',')

print('DataSet tokenized')
