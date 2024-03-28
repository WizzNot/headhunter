import math
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def get_area(self) -> float:
        pass
    

class Circle(Shape):
    def __init__(self, radius: float):
        if radius <= 0:
            raise ValueError("Radius must be > 0")
        self.radius = radius

    def get_area(self) -> float:
        return math.pi * (self.radius ** 2)


class Triangle(Shape):
    def __init__(self, a: float, b: float, c: float):
        perimiter = a + b + c
        if any([perimiter - x <= x for x in (a, b, c)]) or any([x <= 0 for x in (a, b, c)]):
            raise ValueError("a triangle with such sides cannot exist")
        self.a = a
        self.b = b
        self.c = c
    
    def get_area(self) -> float:
        p = (self.a + self.b + self.c) / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
    
    def is_rectangular(self) -> bool:
        hypotenuse = -1
        cathetus_1 = -1
        cathetus_2 = -1
        for i in (self.a, self.b, self.c):
            if i > hypotenuse:
                cathetus_1, cathetus_2, hypotenuse = cathetus_2, hypotenuse, i
            elif i > cathetus_2:
                cathetus_1, cathetus_2 = cathetus_2, i
            elif i > cathetus_1:
                cathetus_1 = i
        return hypotenuse ** 2 == cathetus_1 ** 2 + cathetus_2 ** 2


__all__ = [Shape, Circle, Triangle]