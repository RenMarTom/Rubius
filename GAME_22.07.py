from random import randint


class NPC:
    """""Класс для мирного жителя"""

    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def __str__(self):
        return f'Имя: {self.name}, очки здоровья: {self.hp}'

    def attack(self):
        print("I can't attack")
        return 0


class Sword_Man(NPC):
    def __init__(self, name, hp, max_dmg, min_dmg):
        super().__init__(name, hp)
        self.max_dmg = max_dmg
        self.min_dmg = min_dmg

    def attack(self):
        damage = randint(self.min_dmg, self.max_dmg)
        print(f'Мечник {self.name} нанёс {damage} очков урона')
        return damage


class Mage(NPC):
    def __init__(self, name, hp, mana):
        super().__init__(name, hp)
        self.mana = mana

    def attack(self):
        damage = self.mana * 2
        if damage > 0:
            print(f'Маг {self.name} нанёс {damage} очков урона')
            self.mana -= -10
            return damage
        else:
            print(f'У мага {self.name} закончилась мана')


mirn = NPC('Дядя Дима', 15)
sword = Sword_Man('Сталь',100,10,30)
mag = Mage('Инвокер',50,8)

order = [mirn, mag, sword, mag]
for hero in order:
    print(hero)
    hero.attack()
