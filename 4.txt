import csv


with open('magical.csv', encoding='utf-8') as f:
    reader = list(csv.DictReader(f, delimiter=',', quotechar='"'))
    potions = {}
    for i in reader:
        potions[i['magicaPotions']] = potions.get(i['magicaPotions'], 0) + int(i['count'])
classes = {}
for i in potions.keys():
    potion_class = ' '.join(i.split()[1:])
    classes[potion_class] = classes.get(potion_class, {'potions': [], 'count': 0})
    classes[potion_class]['potions'] = classes.get(potion_class)['potions'] + [i.split()[0]]
    classes[potion_class]['count'] = classes.get(potion_class)['count'] + potions[i]
for i in classes.keys():
    print(f""""<{len(classes[i]['potions'])}> зелий класса <{i}>, общее количество зелий <{classes[i]['count']}>""")
with open('count.txt', 'w', encoding='utf-8') as f:
    for i in classes.keys():
        f.write(f"<{len(classes[i]['potions'])}> зелий класса <{i}>, общее количество зелий <{classes[i]['count']}>\n")