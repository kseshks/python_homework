'''аспектно-ориентрованное программирование
декоратор'''

'''def dec(f):
    def func():
        print('hello')
        f()
    return func

@dec
def main():
    print('function')
    
main()'''

'''def dec2(name):
    def dec_int(f):
        def func():
            
            print('hello')
            f()
        return func
    return dec_int

@dec2('PTF')
def main():
    print('function')
    
main()'''


#ооп, наследование, инкапсюляция, полиморфизм

'''class A:
    def __init__(self):
        self.var = 123
        
    def print_name(self):
        print('a')
        
class B(A):
    def __init__(self):
        super().__init__()
    
    def print_name(self):
        print("b")
        
        
a = A()
b = B()

def use_class (a:A):
    a.print_name()
    
use_class(a)
use_class(b)'''


import math

class Figure():
    def __str__(self):
        return f"Фигура: {self.__class__.__name__}"
        
class Rectangle(Figure):
    def __init__(self, x, y, width, height):
        self.x = x  
        self.y = y
        self.width = width
        self.height = height
        
    def perimeter(self):
        return (self.width + self.height)*2
    
    def area(self):
        return self.width * self.height
        
class Circle(Figure):
    def __init__(self, center_x, center_y, radius):
        self.center_x = center_x
        self.center_y = center_y
        self.radius = radius
        
    def perimeter(self):
        return self.radius*2*3.14
    
    def area(self):
        return self.radius**2 * 3.14

class Circle(Figure):
    def __init__(self, center_x, center_y, radius):
        self.center_x = center_x
        self.center_y = center_y
        self.radius = radius
        
    def perimeter(self):
        return self.radius*2*3.14
    
    def area(self):
        return self.radius**2 * 3.14  

        
class Triangle(Figure):
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.x1, self.y1 = x1, y1
        self.x2, self.y2 = x2, y2
        self.x3, self.y3 = x3, y3
        
        self.a = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        self.b = math.sqrt((x3 - x1)**2 + (y3 - y1)**2)
        self.c = math.sqrt((x2 - x3)**2 + (y2 - y3)**2)
        
    def perimeter(self):
        return self.a + self.b + self.c
        
    def area(self):
        p = self.perimeter() / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))  
        
while True:
    print("1 - Прямоугольник, 2 - Круг, 3 - Треугольник")
    choice = input()
    
    if choice == "1":
        print('прямоугольник')
        print("координаты верхнего левого угла и размеры:")
        x = float(input())
        y = float(input())
        width = float(input())
        height = float(input())
        
        rect = Rectangle(x, y, width, height)
        print("Периметр", rect.perimeter())
        print("Площадь", rect.area())
        
    elif choice == "2":
        print('Круг')
        print("Введите центр")
        center_x = float(input())
        center_y = float(input())
        print("радиус")
        radius = float(input())
        
        circle = Circle(center_x, center_y, radius)
        print("Периметр", circle.perimeter())
        print("Площадь", circle.area())
        
    elif choice == "3":
        print('Треугольник')
        print("Введите координаты трех вершин:")
        x1 = float(input())
        y1 = float(input())
        x2 = float(input())
        y2 = float(input())
        x3 = float(input())
        y3 = float(input())
        
        triangle = Triangle(x1, y1, x2, y2, x3, y3)
        print("Периметр", triangle.perimeter())
        print("Площадь", triangle.area())
        
    else:
        break