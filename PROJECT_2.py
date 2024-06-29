people = {}
people_num = ['',0]
t = ["Ребёнок", "Школьник", "Студент", "Работающий", "Пенсионер"]
t1 = ["детей", "школьников", "студентов", "работающих", "пенсионеров"]
num = []
for i in range(5):
    people[t[i]] = []
    for j in range(int(input(f'Введите количество {t1[i]}: '))):
        print(" ")
        print("Введите данные")
        people[t[i]].append([])
        for k in ["фамилию","имя","отчество"]:
            people[t[i]][j].append(input(f'Введите {k}: '))
    if j > people_num[1]:
        people_num[0] = t1[i]
        people_num[1] = j
    print(" ")
print(f'Больше всего {people_num[0]} - {people_num[1]+1}')
