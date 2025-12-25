#Polymorphism

#Program 01

class shapes:
    def __init__(self):
        pass

class Rectangle(shapes):
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    

class Circle(shapes):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius
    


shapes = [
    Rectangle(4, 5),
    Circle(3)
]

for s in shapes:
    print(s.area())