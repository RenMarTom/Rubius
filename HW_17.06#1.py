d = {"дом": 'house', "пять": "5", "1": "True"}
k = 0
for i in ["дом", "пять", "1"]:
    if d[i] in ['house','5','True']:
        k += 1
if k == 3:
    print('ДА')
else:
    print('НЕТ')
