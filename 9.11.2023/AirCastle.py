from dataclasses import dataclass


class AirCastle:
    def __init__(self, height, clouds, color):
        self.height = height
        self.clouds = clouds
        self.color = color


@dataclass
class AirClassData:
    height: int
    clouds: int
    color: str

    def change_height(self, value):
        c = self.clouds + value
        if c < 0:
            c = 0
        self.clouds = c

    def __add__(self, other):
        if not isinstance(other, int):
            raise TypeError('Не тот тип!')
        self.clouds += other
        self.height += other // 5
        return AirClassData(self.clouds, self.height, self.color)

    def opacity(self, degree):
        self.degree = self.height // degree * self.clouds
        print(f'Прозрачность облаков: {self.degree}')

    def __str__(self):
        return f'The castle at an altitube of {self.height} meters is {self.color} with {self.clouds} clouds'

    def __eq__(self, other):
        if not isinstance(other, AirClassData):
            raise TypeError('error')
        return self.clouds == other.clouds

    def __lt__(self, other):
        if not isinstance(other, AirClassData):
            raise TypeError('error')
        return self.clouds < other.clouds

    def __le__(self, other):
        if not isinstance(other, AirClassData):
            raise TypeError('error')
        return self.clouds > other.clouds


castle1 = AirClassData(500, 15, 'green')
castle2 = AirClassData(500, 12, 'orange')

print(castle1)
castle1.change_height(4)
print(castle1)

castle1 = castle1 + 100
print(castle1)

castle1.opacity(4)
print(castle1)

print(castle1 > castle2)
