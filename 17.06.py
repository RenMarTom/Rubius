d = {}
lst = ["+79610","+79614","+37843","+54387","+3987", "+87451"]
b = []
a1 = str
c = 0
for i in range(len(lst)):
    a = lst[i][0:2]
    for j in range (len(lst)):
        if a1 != a:
            if lst[j][0:2] == a:
                d[a] = lst[j]
    a1 = a
print(d)
