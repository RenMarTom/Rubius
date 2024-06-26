from random import randint,choice
names = ['Roman','Mark','Yaroslav','Sofia']
marks = {}
for i in range(50):
    a = choice(names)
    if a in marks:
        marks[a].append(randint(2,5))
    else:
        marks[a] = []
        marks[a].append(randint(2,5))
print(marks)

#рандомно добавлять оценки к именам в виде словаря
