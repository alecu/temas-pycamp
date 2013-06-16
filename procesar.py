import csv
from pprint import pprint
from collections import defaultdict

r = csv.DictReader(open("temas.csv"))
dict_temas = defaultdict(lambda: ([], []))
for row in r:
    apodo = row["apodo"]
    participar = set(row["participar"].replace("Kilink,", "Kilink:").split(", "))
    conocer = set(row["conocer"].replace("Kilink,", "Kilink:").split(", ")) - participar

    for t in participar:
	if t:
            dict_temas[t][0].append(apodo)

    for t in conocer:
	if t:
            dict_temas[t][1].append(apodo)

list_temas = sorted([ (len(participar+conocer), tema, participar, conocer) for tema, (participar, conocer) in dict_temas.items() ], reverse=True)

print 'votos, tema, participar, conocer'
for i in list_temas:
    print i
