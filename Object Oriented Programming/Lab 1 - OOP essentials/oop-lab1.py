from matplotlib import pyplot as plt
from matplotlib.patches import Rectangle
from datetime import datetime as dt
from math import gcd


# Zadanie 1
class Punkt:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def nalezy_do(self, other):
        return other.a * self.x + other.b == self.y


class Prosta:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def miejsce_zerowe(self):
        return int((-1 * self.b) / self.a)


'''
p = Punkt(3, 6)
pr = Prosta(2, 0)

print(p.nalezy_do(pr))
print(pr.miejsce_zerowe())
'''


# Zadanie 2
class Prostokat:
    def __init__(self, obj1, obj2):
        self.x = [obj1.x, obj2.x]
        self.y = [obj1.y, obj2.y]
        self.height = abs(obj2.y - obj1.y)
        self.width = abs(obj2.x - obj1.x)

    def pole(self):
        return self.height * self.width

    def obwod(self):
        return 2 * self.height + 2 * self.width

    def rysuj(self):
        plt.axis([0, self.x[1] + 4, 0, self.y[0] + 3])
        plt.scatter(self.x, self.y, s=80, zorder=2)
        plt.gca().add_patch(
            Rectangle(
                (self.x[0], self.y[0]),
                self.width,
                self.height,
                linewidth=1.5,
                fill=None,
                alpha=1,
                color='C0',
                zorder=2
            )
        )
        plt.grid(linestyle='--')
        plt.show()


'''
p1 = Punkt(1, 1)
p2 = Punkt(2, 3)
prost = Prostokat(p1, p2)

prost.pole()
prost.obwod()
prost.rysuj()
'''


# Zadanie 3
class Note:
    def __init__(self, who, what):
        self.who = who
        self.what = what
        self.curr_time = dt.now().strftime("%H:%M")

    def __str__(self):
        return f'{self.who}: "{self.what}" o godzinie {self.curr_time}'


class Notebook:
    def __init__(self):
        self.note_list = []

    def dodaj_nowa(self, who, what):
        self.note_list.append(f'{who}: "{what}" o godzinie {dt.now().strftime("%H:%M")}')

    def dodaj(self, note: Note):
        self.note_list.append(note)

    def wyswietl_wszystko(self):
        print('Masz takie notatki:')
        for i in range(len(self.note_list)):
            print(f'{i+1}. {self.note_list[i]}')


'''
nb = Notebook()
nb.dodaj_nowa("Bartek", "SDGHSGDHSGDS")
nb.wyswietl_wszystko()
n1 = Note("Andrii", "SKDJSKJDKSJKDJ")
nb.dodaj(n1)
nb.wyswietl_wszystko()
'''


# Zadanie 4
class Fraction:
    def __init__(self, a, b):
        self.__nmr = a
        self.__dnm = b
        div = gcd(self.nmr, self.dnm)
        self.__nmr //= div
        self.__dnm //= div

    @property
    def nmr(self):
        return self.__nmr

    @property
    def dnm(self):
        return self.__dnm

    def __str__(self):
        try:
            whole = int(self.nmr / self.dnm)
            numerator = self.nmr % self.dnm

            if whole == 0:
                return f"{numerator}/{self.dnm}"
            elif numerator == 0:
                return f"{whole}"
            else:
                return f"{whole} {numerator}/{self.dnm}"

        except ZeroDivisionError:
            return "Nie można dzielić przez zero!"

    def __repr__(self):
        rpr = f"Fraction({self.nmr}, {self.dnm})"
        return rpr

    def __add__(self, other):
        return Fraction(self.nmr * other.dnm + other.nmr * self.dnm, self.dnm * other.dnm)

    def __sub__(self, other):
        return Fraction(self.nmr * other.dnm - other.nmr * self.dnm, self.dnm * other.dnm)

    def __mul__(self, other):
        return Fraction(self.nmr * other.nmr, self.dnm * other.dnm)

    def __truediv__(self, other):
        return Fraction(self.nmr * other.dnm, self.dnm * other.nmr)

    def __abs__(self):
        return Fraction(abs(self.nmr), abs(self.dnm))

    def __lt__(self, other):
        return self.nmr / self.dnm < other.nmr / other.dnm

    def __le__(self, other):
        return self.nmr / self.dnm <= other.nmr / other.dnm

    def __eq__(self, other):
        return self.nmr / self.dnm == other.nmr / other.dnm

    def __ne__(self, other):
        return self.nmr / self.dnm != other.nmr / other.dnm

    def __gt__(self, other):
        return self.nmr / self.dnm > other.nmr / other.dnm

    def __ge__(self, other):
        return self.nmr / self.dnm >= other.nmr / other.dnm

    def __float__(self):
        return float(self.nmr / self.dnm)

    def __int__(self):
        return int(self.nmr / self.dnm)

    def __bool__(self):
        return bool(self.nmr / self.dnm)

    def __round__(self, n=2):
        return round(float(self.nmr / self.dnm))


'''
f = Fraction(1, 3)
print(repr(f))
print(f)
f2 = Fraction(5, 4)
print(f2)
'''