class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        print("length and width are set")
    
    def calc_area(self):
        return self.length * self.width
    def calc_peri(self):
        return 2 * (self.length + self.width)
rec1 = Rectangle(2,3)
print(rec1)
print(rec1.calc_area())
print(rec1.calc_peri())
    
        