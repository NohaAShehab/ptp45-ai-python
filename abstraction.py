
from abc import  ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass


# s = Shape()
# TypeError: Can't instantiate abstract class Shape without an
# implementation for abstract method 'calculate_area'

"inherit from shape"
class Square(Shape):
    def __init__(self, side):
        self.side = side
    def calculate_area(self):
        return self.side * self.side

mysquare = Square(4)
print(mysquare.calculate_area())