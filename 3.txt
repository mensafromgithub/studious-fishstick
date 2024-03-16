import csv


with open('magical.csv', encoding='utf-8') as f:
    reader = list(csv.DictReader(f, delimiter=',', quotechar='"'))
    potions = {}
    for i in reader:
        potions[i['magicaPotions']] = potions.get(i['magicaPotions'], 0) + int(i['count'])
magic_herbs_3 = input()
while magic_herbs_3 != 'стоп':
    ch_potions = []
    for i in range(len(reader)):
        if reader[i]['magic_herbs_3'] == magic_herbs_3:
            ch_potions += [[reader[i]['magicaPotions'], potions[reader[i]['magicaPotions']]]]
    if ch_potions:
        trava = sorted(ch_potions, key=lambda x: x[1])[-1]
        print(f"По вашему запросу <{magic_herbs_3}> найден следующий вариант: <{magic_herbs_3}> используется в <{trava[0]}>, его количество составляет : <{trava[1]}>")
    else:
        print('Такую траву мы не используем')
    magic_herbs_3 = input()