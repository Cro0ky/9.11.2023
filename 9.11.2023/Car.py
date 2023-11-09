from dataclasses import dataclass, make_dataclass, field


class Car:
    def __init__(self, model, max_speed, price):
        self.model = model
        self.max_speed = max_speed
        self.price = price

    def get_max_speed(self):
        return self.max_speed


@dataclass
class CarData:
    model: str
    max_speed: int
    price: int | float = 0

    def get_max_speed(self):
        return self.max_speed


CarDataNew = make_dataclass('CarDataNew', [('model', str),
                                           'max_speed',
                                           ('price', int | float, field(default=0))],
                            namespace={'get_max_speed': lambda self: self.max_speed})


car = Car('nisan', 210, 2000000)
print(car.__dict__)
car2 = CarData('audi', 150, 1000000)
print(car2.__dict__)
car3 = CarDataNew('noname', 123, 1212123.32)
print(car3.__dict__)
