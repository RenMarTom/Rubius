class Transport:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    def information(self):
        return f'{self.brand} {self.model}, {self.year} года'

class Car(Transport):
    def __init__(self, brand, model, year, doors):
        super().__init__(brand, model, year)
        self.doors = doors
    def information(self):
        return f'{self.doors} двери'

class Plane(Transport):
    def __init__(self, brand, model, year, pax):
        super().__init__(brand, model, year)
        self.pax = pax
    def information(self):
        return f'{self.pax} пассажиров'

class Ship(Transport):
    def __init__(self, brand, model, year, engine):
        super().__init__(brand, model, year)
        self.engine = engine
    def information(self):
        return f'{self.engine} двигатель'

c1 = Car('Toyota','LC200',2015,4)
print(c1.information())
pl1 = Plane('Boeing','737',2000, 200)
print(pl1.information())
sh1 = Ship('Titanik','','1900','Дизельный')
print(sh1.information())
