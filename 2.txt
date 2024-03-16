import csv


with open('magical.csv', encoding='utf-8') as f:
    reader = list(csv.DictReader(f, delimiter=',', quotechar='"'))
    potions = {}
    for i in reader:
        potions[i['magicaPotions']] = potions.get(i['magicaPotions'], 0) + int(i['count'])
potions = [(i, potions[i]) for i in potions.keys()]
for i in range(len(potions)):
    n = i - 1
    key = potions[i]
    while potions[n][1] < key[1] and n >=0:
        potions[n + 1] = potions[n]
        n -= 1
    potions[n + 1] = key
potions = potions[::-1]
for i in range(5):
    print(f"Зелья <{potions[i][0]}> осталось <{potions[i][1]}>")
with open('sorted.txt', 'w', encoding='utf-8') as f:
    for i in range(5):
        f.write(f'Зелья <{potions[i][0]}> осталось <{potions[i][1]}>\n')