a = 'Python 3.9.11 - best language!'
b = []
for i in range(len(a)):
    if a[i].isdigit() == 1:
       b.append(a[i])
print(set(b))
