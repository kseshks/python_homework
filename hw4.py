# geometry
# #классы ui

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


class DrawingCanvas:
    def __init__(self, parent, width=400, height=400):
        self.canvas = tk.Canvas(parent, width=width, height=height, bg="white")
        self.canvas.pack(pady=10)
        
    def draw_circle(self, x, y, radius, color="blue"):
        self.canvas.create_oval(x - radius, y - radius, x + radius, y + radius, 
                               outline=color, width=2)
        
    def draw_rectangle(self, x, y, width, height, color="green"):
        self.canvas.create_rectangle(x, y, x + width, y + height, 
                                   outline=color, width=2)
        
    def draw_triangle(self, x1, y1, x2, y2, x3, y3, color="red"):
        self.canvas.create_polygon(x1, y1, x2, y2, x3, y3, 
                                  outline=color, fill="", width=2)
        
    def clear(self):
        self.canvas.delete("all")


class ShapeDialog:
    @staticmethod
    def get_circle_params():
        x = simpledialog.askinteger("Круг", "Введите координату X центра:")
        y = simpledialog.askinteger("Круг", "Введите координату Y центра:")
        r = simpledialog.askinteger("Круг", "Введите радиус:")
        return x, y, r
    
    @staticmethod
    def get_rectangle_params():
        x = simpledialog.askinteger("Прямоугольник", "Введите координату X левого верхнего угла:")
        y = simpledialog.askinteger("Прямоугольник", "Введите координату Y левого верхнего угла:")
        width = simpledialog.askinteger("Прямоугольник", "Введите ширину:")
        height = simpledialog.askinteger("Прямоугольник", "Введите высоту:")
        return x, y, width, height
    
    @staticmethod
    def get_triangle_params():
        x1 = simpledialog.askinteger("Треугольник", "Введите x1:")
        y1 = simpledialog.askinteger("Треугольник", "Введите y1:")
        x2 = simpledialog.askinteger("Треугольник", "Введите x2:")
        y2 = simpledialog.askinteger("Треугольник", "Введите y2:")
        x3 = simpledialog.askinteger("Треугольник", "Введите x3:")
        y3 = simpledialog.askinteger("Треугольник", "Введите y3:")
        return x1, y1, x2, y2, x3, y3


class ShapeInfoDialog:
    @staticmethod
    def show_circle_info(circle):
        messagebox.showinfo(
            "Информация о круге",
            f"Площадь: {circle.area():.2f}\nПериметр: {circle.perimeter():.2f}"
        )
    
    @staticmethod
    def show_rectangle_info(rectangle):
        messagebox.showinfo(
            "Информация о прямоугольнике",
            f"Площадь: {rectangle.area():.2f}\nПериметр: {rectangle.perimeter():.2f}"
        )
    
    @staticmethod
    def show_triangle_info(triangle):
        messagebox.showinfo(
            "Информация о треугольнике",
            f"Площадь: {triangle.area():.2f}\nПериметр: {triangle.perimeter():.2f}"
        )


class Panel:
    def __init__(self, parent, drawing_canvas):
        self.parent = parent
        self.drawing_canvas = drawing_canvas
        self.frame = tk.Frame(parent)
        self.frame.pack(pady=10)
        
    def create_buttons(self):
        btn_circle = tk.Button(self.frame, text="Нарисовать круг", 
                              command=self.draw_circle, width=20, height=2)
        btn_circle.pack(pady=5)
        
        btn_rectangle = tk.Button(self.frame, text="Нарисовать прямоугольник", 
                                 command=self.draw_rectangle, width=20, height=2)
        btn_rectangle.pack(pady=5)
        
        btn_triangle = tk.Button(self.frame, text="Нарисовать треугольник", 
                                command=self.draw_triangle, width=20, height=2)
        btn_triangle.pack(pady=5)
        
        btn_clear = tk.Button(self.frame, text="Очистить", 
                             command=self.drawing_canvas.clear, width=20, height=2)
        btn_clear.pack(pady=5)
        
    def draw_circle(self):
        params = ShapeDialog.get_circle_params()
        if all(param is not None for param in params):
            x, y, r = params
            circle = Circle(x, y, r)
            self.drawing_canvas.draw_circle(x, y, r)
            ShapeInfoDialog.show_circle_info(circle)
    
    def draw_rectangle(self):
        params = ShapeDialog.get_rectangle_params()
        if all(param is not None for param in params):
            x, y, width, height = params
            rectangle = Rectangle(x, y, width, height)
            self.drawing_canvas.draw_rectangle(x, y, width, height)
            ShapeInfoDialog.show_rectangle_info(rectangle)
    
    def draw_triangle(self):
        params = ShapeDialog.get_triangle_params()
        if all(param is not None for param in params):
            x1, y1, x2, y2, x3, y3 = params
            triangle = Triangle(x1, y1, x2, y2, x3, y3)
            self.drawing_canvas.draw_triangle(x1, y1, x2, y2, x3, y3)
            ShapeInfoDialog.show_triangle_info(triangle)


class MainApplication:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Геометрические фигуры")
        self.root.geometry("500x650")

        self.drawing_canvas = DrawingCanvas(self.root)
        self.control_panel = Panel(self.root, self.drawing_canvas)
        self.control_panel.create_buttons()
        
    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = MainApplication()
    app.run()