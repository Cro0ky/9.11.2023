from dataclasses import dataclass


@dataclass
class Goodifrit:
    height: int
    name: str
    kindness: int

    def change_goodness(self, value):
        c = self.kindness + value
        if c < 0:
            c = 0
        self.kindness = c

    def __add__(self, other):
        if not isinstance(other, int):
            return TypeError('error')
        return Goodifrit(self.height + other, self.name, self.kindness)

    def arguments(self, param):
        return f'{param * self.kindness // self.height}'

    def __str__(self):
        return f'Good Ifrit {self.name}, height {self.height}, goodness {self.kindness}'

    def __eq__(self, other):
        if not isinstance(other, Goodifrit):
            raise TypeError('error')
        return (self.kindness, self.height, self.name) == (other.kindness, other.height, other.name)

    def __lt__(self, other):
        if not isinstance(other, Goodifrit):
            raise TypeError('error')
        return (self.kindness, self.height, self.name) < (other.kindness, other.height, other.name)

    def __le__(self, other):
        if not isinstance(other, Goodifrit):
            raise TypeError('error')
        return (self.kindness, self.height, self.name) > (other.kindness, other.height, other.name)


ifrit = Goodifrit(15, 'name', 5)
ifrit2 = Goodifrit(15, 'name2', 5)
ifrit.change_goodness(4)
print(ifrit)
print(ifrit + 10)
print(ifrit.arguments(5))
print(ifrit > ifrit2)
