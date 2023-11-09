from dataclasses import dataclass


@dataclass
class Wizard:
    name: str
    rank: int
    looksAges: int

    def change_rating(self, value):
        c = self.rank + value
        if c > 100:
            c = 100
            if self.looksAges >= 18:
                self.looksAges = self.looksAges // 10
        elif c < 1:
            c = 1
        print(f'{self.looksAges, self.rank}')

    def __str__(self):
        return f'Wizard {self.name} with {self.rank} rating looks {self.looksAges} years old'

    def __eq__(self, other):
        if not isinstance(other, Wizard):
            raise TypeError('error')
        return (self.rank, self.looksAges, self.name) == (other.rank, other.looksAges, other.name)

    def __lt__(self, other):
        if not isinstance(other, Wizard):
            raise TypeError('error')
        return (self.rank, self.looksAges, self.name) < (other.rank, other.looksAges, other.name)

    def __le__(self, other):
        if not isinstance(other, Wizard):
            raise TypeError('error')
        return (self.rank, self.looksAges, self.name) > (other.rank, other.looksAges, other.name)


wizzard = Wizard('name', 200, 28)
wizzard.change_rating(5)
print(wizzard)