class Soda:
    def __init__(self, add=''):
        self.add = add


drink = Soda(input())
dr_add = drink.add
print(f'Газировка и {dr_add}') if dr_add != '' else print('Обычная газировка')
