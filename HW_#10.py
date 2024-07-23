def check(a):
    return len(a) >= 6


lst = ['Tomsk', 'Krasnoyarsk', 'Kemerovo', 'Omsk', 'Moscow']
for i in lst:
    if not check(i):
        lst.remove(i)
print(lst)
