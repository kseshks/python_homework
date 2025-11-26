#cube
import math
import tkinter as tk

class Mat:
    def __init__(self, data):
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0])

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            result = [
                [self.data[i][j] * other for j in range(self.cols)]
                for i in range(self.rows)
            ]
            return Mat(result)
        else:
            if self.cols != other.rows:
                raise ValueError("Размеры матриц не совпадают")
            result = [
                [sum(self.data[i][k] * other.data[k][j] for k in range(self.cols))
                for j in range(other.cols)]
                for i in range(self.rows)
            ]
            return Mat(result)

def rotation_x(angle):
    return Mat([
        [1, 0, 0],
        [0, math.cos(angle), -math.sin(angle)],
        [0, math.sin(angle), math.cos(angle)]
    ])

def rotation_y(angle):
    return Mat([
        [math.cos(angle), 0, math.sin(angle)],
        [0, 1, 0],
        [-math.sin(angle), 0, math.cos(angle)]
    ])

root = tk.Tk()
canvas = tk.Canvas(root, width=600, height=600, bg="white")
canvas.pack()

points = [
    [-1, -1, -1], [1, -1, -1], [-1, 1, -1], [1, 1, -1],
    [-1, -1, 1], [1, -1, 1], [-1, 1, 1], [1, 1, 1]
]

edges = [
    (0, 1), (1, 3), (3, 2), (2, 0),
    (4, 5), (5, 7), (7, 6), (6, 4), 
    (0, 4), (1, 5), (2, 6), (3, 7)  
]

angle_x = 0
angle_y = 0

def draw_cube():
    global angle_x, angle_y
    canvas.delete("all")
    
    rotation = rotation_y(angle_y) * rotation_x(angle_x)
    
    transformed_points = []
    
    for point in points:
        vec = Mat([[point[0]], [point[1]], [point[2]]])
        rotated = rotation * vec
        x, y, z = rotated.data[0][0], rotated.data[1][0], rotated.data[2][0]
        
        scale = 200 / (z + 4)
        x2d = 300 + x * scale
        y2d = 300 + y * scale
        
        transformed_points.append((x2d, y2d))

    for edge in edges:
        p1 = transformed_points[edge[0]]
        p2 = transformed_points[edge[1]]
        canvas.create_line(p1[0], p1[1], p2[0], p2[1], width=2)

    for x, y in transformed_points:
        canvas.create_oval(x-3, y-3, x+3, y+3, fill="black")

    angle_x += 0.02
    angle_y += 0.015
    
    root.after(30, draw_cube)

draw_cube()
root.mainloop()


