'''__mul__
__add__'''

'''class A:
    def __init__(self, val):
        self.__val = val
        self.val = val
        self._val =  val
    def __mul__(self, other):
        self.__val = self.__val * other.__val
        return self
        
        
a = A(5)
b = A(7)
c = a* b 
print(a.__dict__)
print(c.__dict__)
    '''
    
#задание. написать класс для матриц с переопределенными методами сложения и умножения
import math
import tkinter as tk
from tkinter import simpledialog, messagebox

class Mat:
    def __init__(self, data):
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0])

    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError
        result = [
            [self.data[i][j] + other.data[i][j] for j in range(self.cols)] for i in range(self.rows)
        ]
        return Mat(result)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            result = [
                [self.data[i][j] * other for j in range(self.cols)]
                for i in range(self.rows)
            ]
            return Mat(result)
        
        else:
            if self.cols != other.rows:
                raise ValueError
            result = [
                [sum(self.data[i][k] * other.data[k][j] for k in range(self.cols))
                for j in range(other.cols)]
                for i in range(self.rows)
            ]
            return Mat(result)

    def __repr__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.data])
    
A = Mat([
    [1, 2, 3],
    [4, 5, 6]
])

B = Mat([
    [7, 8, 9],
    [10, 11, 12]
])

C = Mat([
    [1, 2],
    [3, 4],
    [5, 6]
])

'''print("A + B =")
print(A + B)

print("\nA * C =")  #22 28
print(A * C)

print("\nA * 2 =")  
print(A * 2)'''

#задание 2. отрисовать вращение кубика относительно двух осей одновременно - X и y. исползовать матрицу поворота:
#(1   0     0)
#(0  cosa sina)  * A
#(0 -sina cosa)
root = tk.Tk()
root.title("Задание №2")
canvas = tk.Canvas(root, width=400, height=400, bg="white")
canvas.pack()

points = [
    [-1,-1,-1],
    [1,-1,-1],
    [-1,1,-1],
    [1,1,-1],
    [-1,-1,1],
    [1,-1,1],
    [-1,1,1],
    [1,1,1],
]

edges = [
    (0, 1), (1, 2), (2, 3), (3, 0),
    (4, 5), (5, 6), (6, 7), (7, 4),
    (0, 4), (1, 5), (2, 6), (3, 7)
]

angle_x = 0
angle_y = 0

def draw_cube():
    global angle_x, angle_y
    canvas.delete("all")
    
    Rx = Mat([
        [1, 0, 0],
        [0, math.cos(angle_x), -math.sin(angle_x)],
        [0, math.sin(angle_x), math.cos(angle_x)]
    ])

    Ry = Mat([
        [math.cos(angle_y), 0, math.sin(angle_y)],
        [0, 1, 0],
        [-math.sin(angle_y), 0, math.cos(angle_y)]
    ])
    
    transformed_points = []
    
    for p in points:
        vec = Mat([[p[0]], [p[1]], [p[2]]])
        rotated = Rx.__mul__(Ry.__mul__(vec))
        x, y, z = rotated.data[0][0], rotated.data[1][0], rotated.data[2][0]
        
        # Простая проекция 3D -> 2D
        scale = 100 / (z + 4)
        x2d = 250 + x * scale * 100
        y2d = 250 + y * scale * 100
        transformed_points.append((x2d, y2d))

    # Рисуем рёбра куба
    for edge in edges:
        p1 = transformed_points[edge[0]]
        p2 = transformed_points[edge[1]]
        canvas.create_line(p1[0], p1[1], p2[0], p2[1], fill="blue", width=2)
    
    # Обновляем углы вращения
    angle_x += 0.05
    angle_y += 0.03
    root.after(50, draw_cube)

draw_cube()
root.mainloop()
    
