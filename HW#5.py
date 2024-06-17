lst = ['Москва', 'Астрахань', 'Новгород', 'Димитровград', 'Душанбе']
k = 0
d = {"а": "А", "н": "Н", "д": "Д"}
for i in range(len(lst) - 1):
    if lst[i][-1] not in ['ь', 'ъ', 'ы'] and d[lst[i][-1]] == lst[i + 1][0]:
        k += 1
    elif lst[i][-1] in ['ь', 'ъ', 'ы'] and d[lst[i][-2]] == lst[i + 1][0]:
        k += 1
if k == len(lst)-1:
    print('ДА')
else:
    print('НЕТ')
