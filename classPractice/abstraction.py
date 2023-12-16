from abc import ABC, abstractmethod
class shape:
    def __init__(self, color) -> None:
        self.color = color
    def get_color(self):
        return self.color
    
    @abstractmethod
    def area(self):
        pass

class square(shape):
    
    def __init__(self, length, color):
        super().__init__(color)
        self.length = length 
        
    def area(self):
        return self.length ** 2
    
class circle(shape):
    def __init__(self, radius, color):
        super().__init__(color)
        self.radius = radius 
    # def area(self):
    #     return (self.radius ** 2) * 3.14
    
circle1 = circle(3, "red")
square1 = square(3, "blue")
print("Circle: ")
print(circle1.area())
print(circle1.color)

print("Square: ")
print(square1.area())
print(square1.color)