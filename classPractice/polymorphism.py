class shape:
    def __init__(self, color) -> None:
        self.color = color
    def get_color(self):
        return self.color
    def area(self):
        pass

def calc_area(shape):
    return shape.area()
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
    def area(self):
        return (self.radius ** 2) * 3.14
    
circle1 = circle(3, "red")
square1 = square(3, "blue")
print("Circle: ")
print(calc_area(circle1))
print(circle1.color)

print("Square: ")
print(calc_area(square1))
print(circle1.color)