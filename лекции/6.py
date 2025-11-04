def counter(f):  # Шаг 1: декоратор получает функцию f
    count = 0    # Шаг 2: создается переменная-счетчик
    
    def res(*args, **kwargs):  # Шаг 3: создается новая функция-обертка
        nonlocal count         # Шаг 4: говорим "используй внешнюю count"
        count += 1            # Шаг 5: увеличиваем счетчик
        print(f"Вызов №{count}")
        return f(*args, **kwargs)  # Шаг 6: вызываем оригинальную функцию
    
    res.call_count = lambda: count  # Шаг 7: добавляем атрибут
    return res          # Шаг 8: возвращаем новую функцию

@counter
def fact(n):
    if n == 1:
        return 1
    else:
        return fact(n - 1) * n

'''# Проверяем
print(f"fact(5) = {fact(5)}")
print(f"Всего вызовов: {fact.call_count()}")'''


def validator(f):
    def res(n):
        if n%1 != 0:
            return TypeError("n должно быть целым числом")
        if n < 0:
            return ValueError("n должно быть положительным")
        return f(n)
    return res



@validator
@counter
def fact(n):
    if n == 1:
        return 1
    else:
        return fact(n - 1) * n
    
print(3%1)
print(1, fact(3))    # должно работать
print(2, fact(-3))   # должно быть ValueError
print(3, fact(2.5))  # должно быть TypeError

class Rectangle:
    def __init__(self, width, height):#конструктор, принимающий ширину и высоту
        self.width = width
        self.height = height
    
    def area(self):
        # метод, возвращающий площадь прямоугольника
        
        return self.width * self.height
    
    def perimeter(self):
        # метод, возвращающий п прямоугольника
        return (self.width + self.height)*2
    
    def __str__(self):
        return f"Прямоугольник {self.width}x{self.height}" #метод, возвращающий строковое представление в формате "Прямоугольник [ширина]x[высота]"
    
rect = Rectangle(5, 3)
print(rect)           # Прямоугольник 5x3
print(rect.area())    # 15
print(rect.perimeter()) # 16