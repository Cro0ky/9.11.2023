from dataclasses import dataclass, field, InitVar


class Vector:

    def __init__(self, x: int, y: int, z: int, calc_len: bool = True):
        self.x = x
        self.y = y
        self.z = z
        self.lenght = ((x ** 2 + y ** 2 + z ** 2) * 0.5) if calc_len else 0


@dataclass(eq=True, order=True)
class VectorData:
    x: int = field(repr=False)
    y: int = field(compare=False)
    z: int = field(default=12)
    calc_len: InitVar[bool] = True
    lenght: float = field(init=False, compare=False, default=0)

    def __post_init__(self, calc_len: bool):
        if calc_len:
            self.lenght = (self.x ** 2 + self.y ** 2 + self.z ** 2) * 0.5


v = Vector(2, 3, 4, calc_len=False)
vd = VectorData(2, 3)
vd2 = VectorData(2, 4, 4)

print(vd.lenght)
print(v.lenght)

print(v.__dict__)
print(vd.__dict__)

print(vd2 <= vd)
