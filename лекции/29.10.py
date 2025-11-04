'''class Test:
    def __init__(self):
        self.h = 123
    @property

    
    from abc import ABC, abstractmethod
class A(ABC):
    @abstabstractmethod
    def hello(self):
        raise NotImplemented()
    
class B(A):
    pass'''

#взять из лекции иерархию классов. добавить класс многоугольни. реалищовать вычисление его площади методом гаусса(0.5 *(x1*y2 - x2*y1 + x2*y3 - x3*y2 + x3*y1 - x1*y3))

'''from abc import ABC, abstractmethod

class figure(ABC):
    def input(self):
        return self
    def __str__(self):
        return ""
    @abstractmethod
    def area(self):
        pass

class point(figure):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def input(self):
        s = input("Введите координаты точки (x y): ").split()
        self.x = float(s[0])
        self.y = float(s[1])
        return self
    
    def __str__(self):
        return f"({self.x},{self.y})"
    
    @property
    def area(self):
        return 0

class polygon(figure):
    def __init__(self, points=None):
        if points is None:
            self.points = []
        else:
            self.points = points
    
    def input(self):
        n = int(input("Введите количество вершин многоугольника: "))
        self.points = []
        for i in range(n):
            print(f"Точка {i+1}: ", end="")
            p = point().input()
            self.points.append(p)
        return self
    
    def __str__(self):
        points_str = ", ".join(str(p) for p in self.points)
        return f"Многоугольник[{points_str}]"
    
    @property
    def area(self):
        if len(self.points) < 3:
            return 0

        n = len(self.points)
        total = 0
        
        for i in range(n):
            x_i = self.points[i].x
            y_i = self.points[i].y
            x_next = self.points[(i + 1) % n].x
            y_next = self.points[(i + 1) % n].y
            
            total += (x_i * y_next - x_next * y_i)
        
        area = 0.5 * abs(total)
        return area

if __name__ == "__main__":
    poly = polygon().input()
    
    print(f"Площадь: {poly.area}")'''
 
 
 
    
#2 написать декоратор, аналогичный декоратору functools.cache, но позволяющий использовать в качестве аргументов функции нехэшируемые типы - список, множество, словарь

'''@mynewcache
def method(1: List):
    return sum(1) ''' 

from functools import wraps

def mynewcache(func):
    cache = {}
    
    @wraps(func)
    def wrapper(*args, **kwargs):
        def make_hashable(item):
            if isinstance(item, (list, tuple)):
                return tuple(make_hashable(e) for e in item)
            elif isinstance(item, set):
                return tuple(sorted(make_hashable(e) for e in item))
            elif isinstance(item, dict):
                return tuple(sorted((make_hashable(k), make_hashable(v)) 
                                  for k, v in item.items()))
            return item
        
        key = (make_hashable(args), make_hashable(kwargs))
        
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]
    
    return wrapper

@mynewcache
def method(lst):
    return sum(lst)

print(method([1, 2, 3]))
print(method([1, 2, 3]))  #из кэша
print(method([4, 5, 6]))
print(method([4, 5, 6]))  #из кэша


print('множества')
@mynewcache
def process_set(s):
    return len(s)

print(process_set({1, 2, 3}))
print(process_set({1, 2, 3}))  #из кэша
print(process_set({3, 2, 1}))  #из кэша


print('словари')
@mynewcache
def process_dict(d):
    return sum(d.values())

print(process_dict({'a': 1, 'b': 2}))
print(process_dict({'a': 1, 'b': 2}))
print(process_dict({'b': 2, 'a': 1}))

