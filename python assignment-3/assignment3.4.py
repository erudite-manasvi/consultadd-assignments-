# Define a class named Shape and its subclass Square. The Square class has an init function which takes length as argument. Both classes have an area function which can print the area of the shape where Shape’s area is 0 by default.

class Shape:
    def __init__(self):
        print('Shape class')

    def area(self):
        return 0

class Square(Shape):
    def __init__(self,length):
        super().__init__()
        print('Square class')
        self.length = length

    def area(self):
        return self.length*self.length

s = Square(10)
print(s.area())

# print(Shape().area())