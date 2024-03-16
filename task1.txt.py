import csv


with open('magical.csv', encoding='utf-8') as f:
    reader = list(csv.DictReader(f, delimiter=',', quotechar='"'))
    potions = {}
    for i in reader:
        potions[i['magicaPotions']] = potions.get(i['magicaPotions'], 0) + int(i['count'])
    for i in potions.keys():
        if potions[i] == 1:
            potions[i] = 0
with open('magicaPotions.txt', 'w', encoding='utf-8') as f:
    for i in potions.keys():
        f.write(f'<{i}> в запасах еще есть - <{potions[i]}>\n')
with open('count_potions.txt', 'w', encoding='utf-8') as f:
    f.write(f"Данного зелья осталось - <{potions['Мощное Зелье']}>\n")
print(f"Данного зелья осталось - <{potions['Мощное Зелье']}>")