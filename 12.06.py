# a = [[], [], [], []]
# for i in range(4):
#     for j in range(i + 1):
#         a[i].append(i + 1)
# print(a)

a = [[], [], [], []]
i = 0
while i < 4:
    j = 0
    while j < (i + 1):
        a[i].append(i + 1)
        j += 1
    i += 1
print(a)
