from abc import ABC, abstractmethod
from math import sqrt
import random as r


# Zadanie 1

class Ssak:
    rodzaj = 'Ssak'

    def __init__(self, info='Brak ciekawostki'):
        self.info = info
        print(f'Stworzyłeś: {self.rodzaj}')

    def ciekawostka(self):
        print(self.info)


class Krowa(Ssak):
    rodzaj = 'Krowa'

    def __init__(self):
        super().__init__(info='Ma rogi.')


class Tygrys(Ssak):
    rodzaj = 'Tygrys'

    def __init__(self):
        super().__init__(info='Ma pazury.')


# Zadanie 2

class GameObject:
    def __init__(self, hp=int()):
        self.hp = hp

    def isalive(self):
        return self.hp > 0

    @abstractmethod
    def interact(self, obj):
        pass


class Player(GameObject):
    def interact(self, obj):
        pass


class Monster(GameObject):
    def interact(self, obj):
        obj.hp -= 10
        self.hp = 0
        print("Potwór został zabity przez gracza")


class Door(GameObject):
    def interact(self, obj):
        print("Gracz przeszedł przez drzwi")


player = Player(50)

obj_quantity = 10   # liczba obiektów
obj_list = []

monster_chance = round(r.random(), 1)   # szansa na potwora w %
door_chance = round(1 - monster_chance, 1)  # szansa na drzwi w %

for i in range(0, int(obj_quantity * monster_chance)):
    obj_list.append(Monster())

for j in range(0, int(obj_quantity * door_chance)):
    obj_list.append(Door())

for item in obj_list:
    item.interact(player)
    if not player.isalive():
        print('Gracz został zabity!')
        break


# Zadanie 3

class Equation(ABC):
    def __init__(self, lst):
        self.params = lst

    @abstractmethod
    def solve(self):
        pass


class LinearEquation(Equation):
    def __init__(self, lst):
        super().__init__(lst)
        if len(lst) == 2:
            self.a = lst[0]
            self.b = lst[1]

    def solve(self):
        try:
            if self.a == 0:
                if self.b != 0:
                    print('Równanie sprzeczne.')
                else:
                    print('Równanie tożsamościowe.')
            else:
                x = int(-self.b / self.a)
                print(f'x = {x}')
        except AttributeError:
            print('Liczba współczynników różna od 2!')


class QuadraticEquation(Equation):
    def __init__(self, lst):
        super().__init__(lst)
        if len(lst) == 3:
            self.a = lst[0]
            self.b = lst[1]
            self.c = lst[2]

    def solve(self):
        try:
            delta = self.b ** 2 - 4 * self.a * self.c
            if delta > 0:
                x1 = int((-self.b - sqrt(delta)) / 2 * self.a)
                x2 = int((-self.b + sqrt(delta)) / 2 * self.a)
                print(f'x1 = {x1}, x2 = {x2}')
            elif delta == 0:
                x = int(-self.b / (2 * self.a))
                print(f'x = {x}')
            else:
                print('Delta ujemna. Brak rozwiązań.')
        except AttributeError:
            print('Liczba współczynników różna od 3!')


eq = LinearEquation([2, 0])
eq.solve()
eq1 = LinearEquation([0, 2])
eq1.solve()
eq2 = QuadraticEquation([1, -5, 6])
eq2.solve()