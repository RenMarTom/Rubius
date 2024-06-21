a = 'Python 3.9.11 - best language!'
b = []
for i in range(len(a)):
    if a[i].isdigit() == 1 and a[i] not in [a[i+1],a[i-1]]:
       b.append(a[i])
print(b)
