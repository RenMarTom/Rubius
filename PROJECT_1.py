number = int(input('Введите количество магазинов: '))
shops = []
shops_l = {}
spisok = []
k = 0
for i in range(number):
    shops.append(input('Введите название магазина: '))
for i in range(number):
    k = 0
    shops_l[shops[i]] = []
    print(f'Магазин {shops[i]}')
    for j in range(int(input('Введите количество товара: '))):
        shops_l[shops[i]].append([])
        a = input('Введите название товара: ')
        shops_l[shops[i]][k].append(a)
        spisok.append(a)
        shops_l[shops[i]][k].append(int(input('Введите количество товара: ')))
        k += 1
spisok = set(spisok)

tovar1 = ['', 0]
tovar = input('Введите необходимый товар: ')
while tovar != 0:
    if tovar not in spisok:
        print('Такого товара нет!')
    for i in shops:
        for j in range(len(shops_l[i])):
            if shops_l[i][j][0] == tovar and shops_l[i][j][1] > tovar1[1]:
                tovar1[0] = i
                tovar1[1] = shops_l[i][j][1]
    print(f'Больше всего товара в магазине {tovar1[0]},количество - {tovar1[1]}')
