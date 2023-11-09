from dataclasses import dataclass, field
from typing import Any
import random


class GoodsMethodsFactory:

    @staticmethod
    def get_init_measure():
        return [0, 0, 0]


@dataclass
class Goods:
    current_uid = 0

    uid: int = field(init=False)
    price: Any
    weight: Any

    def __post_init__(self):
        print('Goods: post_init')
        Goods.current_uid += 1
        self.uid = Goods.current_uid


@dataclass
class Book(Goods):
    title: str = ''
    author: str = ''
    price: float = 0
    weight: int | float = 0
    measure: list = field(default_factory=GoodsMethodsFactory.get_init_measure)

    # super().__init__(1,2,3)
    # self.4 = 4

    def __post_init__(self):
        super().__post_init__()
        print('Book: post_init')


g = Goods('1245 p', 21)
print(g)

g2 = Goods(14, 21)
print(g2)

b = Book(221, 1, 'title', 'author')
b.measure = [(random.randint(1, 15)) for i in range(3)]
print(b)
