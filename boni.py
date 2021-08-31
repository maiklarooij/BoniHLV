import pandas as pd

header_list = ['Hoofdgroep', 'Omschrijving2', 'Boe', 'Bah', 'Nummer', 'Omschrijving', 'Colli']
df = pd.read_csv('bonicolli.csv', names=header_list).drop_duplicates()

cluster1 = df[df['Nummer'].isin([19, 29, 35])]['Colli'].map(lambda x: int(x)).sum()
cluster2 = df[df['Nummer'].isin([1, 2, 13, 15, 16, 18])]['Colli'].map(lambda x: int(x)).sum()
cluster3 = df[df['Nummer'].isin([5, 14, 23, 24, 25, 26, 28, 30])]['Colli'].map(lambda x: int(x)).sum()
cluster4 = df[df['Nummer'].isin([3, 4, 9, 10, 11, 12])]['Colli'].map(lambda x: int(x)).sum()
cluster5 = df[df['Nummer'].isin([7, 8, 17, 20])]['Colli'].map(lambda x: int(x)).sum()

print('Cluster 1 (Frisdrank, Bier, Houdbare Melk): ' + str(cluster1))
print('Cluster 2 (Snoep en Koek): ' + str(cluster2))
print('Cluster 3 (Cosmetica, Soep en Tandpasta): ' + str(cluster3 ))
print('Cluster 4 (Conimex, Groenten in Blik, Pasta, Frituur): ' + str(cluster4))
print('Cluster 5 (Chips, Wijn, Afbakbrood en Ontbijt): ' + str(cluster5))
print('Totaal: ' + str(cluster1 + cluster2 + cluster3 + cluster4 + cluster5))