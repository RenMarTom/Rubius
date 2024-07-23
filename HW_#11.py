def str(a, tag='h1'):
    return f'<{tag}>{a}</{tag}>'


a = input()
print(str(a))
print(str(a, 'div'))
