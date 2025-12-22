#Polymorphism

#Program 01

class shape:
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    


class rectangle(shape):
    def area(self,r,pi = 3.14):
        return pi * (r)^2