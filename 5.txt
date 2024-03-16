import csv


with open('magical.csv', encoding='utf-8') as f:
    reader = list(csv.DictReader(f, delimiter=',', quotechar='"'))
    potions = {}
    for i in reader:
        potions[i['magicaPotions']] = potions.get(i['magicaPotions'], 0) + int(i['count'])
trava = {}
for i in range(len(reader)):
    for j in range(1, 4):
        trava[reader[i][f'magic_herbs_{j}']] = trava.get(reader[i][f'magic_herbs_{j}'], 0) + 1
trava = sorted([(i, trava[i]) for i in trava.keys()], key=lambda x: x[1])
print(trava)
for i in range(1, 6):
    print(f"<{trava[-i][0]}> - <{trava[-i][1]}>.")
with open('top5.txt', 'w', encoding='utf-8') as f:
    for i in range(5):
        f.write(f"<{trava[-i][0]}> - <{trava[-i][1]}>.\n")