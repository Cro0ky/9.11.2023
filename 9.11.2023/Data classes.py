from dataclasses import dataclass, field
from pprint import pprint


class Thing:

    def __init__(self, name, weight, price):
        self.name = name
        self.weight = weight
        self.price = price

    def __repr__(self):
        return f'name - {self.name}, weight - {self.weight}, price - {self.price}'


@dataclass
class ThingData:
    name: str
    weight: int
    price: float
    dims: list = field(default_factory=list)

    def __eq__(self, other):
        return self.price == other.price


t = Thing('name', 1, 1499)
td = ThingData('name', 1, 1499.0)
td2 = ThingData('name2', 12, 1499.02)
print(t)

td.dims.append(20)
print(td)

print(td2)
# pprint(ThingData.__dict__)
print(td == td2)
