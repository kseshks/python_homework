# продолжение классной работы с 22.10

'''К заданию №2

import tkinter as tk
from tkinter import simpledialog

def draw_circle():
    x = simpledialog.askinteger("Круг", "Введите X")
    y = simpledialog.askinteger("Круг", "Введите Y")

    canvas.create_oval(100, 100, 100 + x, 100 + y)
    # canvas.create_rectangle(50, 50, 150, 100)
    # canvas.create_polygon(100, 50, 50, 150, 150, 150)

root = tk.Tk()
canvas = tk.Canvas(root, width=300, height=300, bg="white")
canvas.pack(pady=10)

button = tk.Button(root, text="Нарисовать круг", command=draw_circle)
button.pack(pady=10)

root.mainloop()'''

import math
import tkinter as tk
from tkinter import simpledialog, messagebox

class Figure:
    def area(self):
        return 0

    def perimeter(self):
        return 0


class Rectangle(Figure):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


class Circle(Figure):
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius


class Triangle(Figure):
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.x1, self.y1 = x1, y1
        self.x2, self.y2 = x2, y2
        self.x3, self.y3 = x3, y3

        self.a = math.dist((x1, y1), (x2, y2))
        self.b = math.dist((x2, y2), (x3, y3))
        self.c = math.dist((x3, y3), (x1, y1))

    def area(self):
        p = self.perimeter() / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    def perimeter(self):
        return self.a + self.b + self.c


#2

def draw_circle():
    x = simpledialog.askinteger("Круг", "Введите координату X центра:")
    y = simpledialog.askinteger("Круг", "Введите координату Y центра:")
    r = simpledialog.askinteger("Круг", "Введите радиус:")

    circle = Circle(x, y, r)
    canvas.create_oval(x - r, y - r, x + r, y + r, outline="blue")

    messagebox.showinfo(
        "Информация о круге",
        f"Площадь: {circle.area():.2f}\nПериметр: {circle.perimeter():.2f}"
    )


def draw_rectangle():
    x = simpledialog.askinteger("Прямоугольник", "Введите координату X левого верхнего угла:")
    y = simpledialog.askinteger("Прямоугольник", "Введите координату Y левого верхнего угла:")
    width = simpledialog.askinteger("Прямоугольник", "Введите ширину:")
    height = simpledialog.askinteger("Прямоугольник", "Введите высоту:")

    rect = Rectangle(x, y, width, height)
    canvas.create_rectangle(x, y, x + width, y + height, outline="green")

    messagebox.showinfo(
        "Информация о прямоугольнике",
        f"Площадь: {rect.area():.2f}\nПериметр: {rect.perimeter():.2f}"
    )


def draw_triangle():
    x1 = simpledialog.askinteger("Треугольник", "Введите x1:")
    y1 = simpledialog.askinteger("Треугольник", "Введите y1:")
    x2 = simpledialog.askinteger("Треугольник", "Введите x2:")
    y2 = simpledialog.askinteger("Треугольник", "Введите y2:")
    x3 = simpledialog.askinteger("Треугольник", "Введите x3:")
    y3 = simpledialog.askinteger("Треугольник", "Введите y3:")

    triangle = Triangle(x1, y1, x2, y2, x3, y3)
    canvas.create_polygon(x1, y1, x2, y2, x3, y3, outline="red", fill="")

    messagebox.showinfo(
        "Информация о треугольнике",
        f"Площадь: {triangle.area():.2f}\nПериметр: {triangle.perimeter():.2f}"
    )

root = tk.Tk()
root.title("Задание №2")
canvas = tk.Canvas(root, width=400, height=400, bg="white")
canvas.pack(pady=10)

btn_circle = tk.Button(root, text="Нарисовать круг", command=draw_circle)
btn_circle.pack(pady=5)

btn_rectangle = tk.Button(root, text="Нарисовать прямоугольник", command=draw_rectangle)
btn_rectangle.pack(pady=5)

btn_triangle = tk.Button(root, text="Нарисовать треугольник", command=draw_triangle)
btn_triangle.pack(pady=5)

root.mainloop()


