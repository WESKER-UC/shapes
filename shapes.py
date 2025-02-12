import math as m
class Circle:
    def __init__(self,radius):
        self.radius=radius
        
    def __str__(self):
        return f"<class 'Circle'> Radius({self.radius})"
    def area(self):
        return m.pi*self.radius**2

    def diam(self):
        return self.radius*2
    
    def circum(self):
        return 2*m.pi*self.radius
    
class Rectangle:
    def __init__(self,length,breadth):
        if (breadth>length):
            self.length=breadth
            self.breadth=length
        else:
            self.length=length
            self.breadth=breadth
    
    def __str__(self):
        return f"<class 'Rectangle'> Length({self.length}) Breadth({self.breadth})"
    
    def area(self):
        return self.length*self.breadth

    def diagLen(self):
        return (self.length**2+self.breadth**2)**.5
    
    def peri(self):
        return (self.length+self.breadth)*2
    
    def isSquare(self):
        return 1 if self.length==self.breadth else 0

class Square:

    def __init__(self,side):
        self.side=side
    
    def __str__(self):
        return f"<class 'Square'> Length({self.length})"
    
    def area(self):
        return self.side*self.side

    def diagLen(self):
        return self.side*(2**.5)
    
    def peri(self):
        return 4*self.side
    
    def isSquare(self):
        return 1

class iPolygon:
    def __init__(self, *sides):
        self.sides = sides  

    def perimeter(self):
        return sum(self.sides)  

    def isRegular(self):
        return len(set(self.sides)) == 1 

    def __str__(self):
        return f"<class 'Polygon'> Sides({self.sides})"


class rPolygon:
    def __init__(self, *sides):
        self.sides = sides  

    def perimeter(self):
        return sum(self.sides)  

    def isRegular(self):
        return 1  

    def __str__(self):
        return f"<class 'Polygon'> Sides({self.sides})"
