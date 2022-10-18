import pandas as pd

#pip install sklearn
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import pairwise_distances

dataSteamDataset = pd.read_csv('SteamGames_Description_Tokenized.csv') 

bagOfWordsModel = TfidfVectorizer()
bagOfWordsModel.fit(dataSteamDataset['processed_text'])
textsBoW= bagOfWordsModel.transform(dataSteamDataset['processed_text'])

print("Bag of Words Finished")

# Calculate the distance TODO crear vector de atributos
distance_matrix= pairwise_distances(textsBoW,textsBoW ,metric='cosine')

print(distance_matrix.shape)
print(type(distance_matrix))

# Description
searchDescription= " About This Game The Devil you know returns in this brand new entry in the over-the-top action series available on the PC. Prepare to get downright demonic with this signature blend of high-octane stylized action and otherworldly & original characters the series is known for. Director Hideaki Itsuno and the core team have returned to create the most insane, technically advanced and utterly unmissable action experience of this generation! The threat of demonic power has returned to menace the world once again in Devil May Cry 5 . The invasion begins when the seeds of a “demon tree” take root in Red Grave City. As this hellish incursion starts to take over the city, a young demon hunter Nero, arrives with his partner Nico in their “Devil May Cry” motorhome. Finding himself without the use of his right arm, Nero enlists Nico, a self-professed weapons artist, to design a variety of unique mechanical Devil Breaker arms to give him extra powers to take on evil demons such as the blood sucking flying Empusa and giant colossus enemy Goliath. FEATURES High octane stylized action – Featuring three playable characters each with a radically different stylish combat play style as they take on the city overrun with demons Groundbreaking graphics – Developed with Capcom’s in-house proprietary RE engine, the series continues to achieve new heights in fidelity with graphics that utilize photorealistic character designs and stunning lighting and environmental effects. Take down the demonic invasion – Battle against epic bosses in adrenaline fueled fights across the over-run Red Grave City all to the beat of a truly killer soundtrack. Demon hunter – Nero, one of the series main protagonists and a young demon hunter who has the blood of Sparda, heads to Red Grave City to face the hellish onslaught of demons, with weapons craftswoman and new partner-in-crime, Nico. Nero is also joined by stylish, legendary demon hunter, Dante and the mysterious new character, V. "

indexOfDescription = dataSteamDataset[dataSteamDataset['game_description']==searchDescription].index.values[0]

distance_scores = list(enumerate(distance_matrix[indexOfDescription]))

ordered_scores = sorted(distance_scores, key=lambda x: x[1])

top_scores = ordered_scores[1:11]
top_indexes = [i[0] for i in top_scores]



print(dataSteamDataset['name'].iloc[top_indexes])

# TODO Ampliaciones Django: Framework Python para Web
