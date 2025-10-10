'''ДЗ3 Рекурсия
Задан лабиринт 10x10 клеток (пример ниже)
В нем начальная клетка - 'S', конечная - 'E', стены - '#', пустое место - проходы. Пройти из начала в конец с помощью рекурсии.

##########
####S  ###
###  #####
#### ###E#
###  ##  #
##  ###  #
###  #  ##
####   ###
###### ###
##########'''

maze = [
    "##########",
    "####S  ###",
    "###  #####",
    "#### ###E#",
    "###  ##  #",
    "##  ###  #",
    "###  #  ##",
    "####   ###",
    "###### ###",
    "##########"
]

#мой пример для проверки кротчайшего пути
'''maze = [
    "##########",
    "####S    #",
    "###  ### #",
    "#### ###E#",
    "###  ##  #",
    "##  ###  #",
    "###  #  ##",
    "####   ###",
    "###### ###",
    "##########"
]'''

maze = [list(row) for row in maze]

rows = len(maze)
cols = len(maze[0])

#print(rows,cols)

start = None
end = None

for i in range(rows):
    for j in range(cols):
        if maze[i][j] == 'S':
            start = (i, j)
        elif maze[i][j] == 'E':
            end = (i, j)

paths = []
def find_way(x, y, path):
    
    if x < 0 or x > rows or y < 0 or y > cols:
        return False
    if maze[x][y] == '#' or maze[x][y] == 'v':
        return False
    if maze[x][y] == 'E':
        paths.append(path.copy())
        return True
    
    temp = maze[x][y]
    maze[x][y] = 'v' #visited
    path.append((x, y))
    
    find_way(x - 1, y, path)
    find_way(x + 1, y, path)
    find_way(x, y + 1, path)
    find_way(x, y - 1, path)
    
    maze[x][y] = temp
    path.pop()
  
find_way(*start, [])

if paths:
    shortest = min(paths, key=len)
    
    for (x, y) in shortest:
        if maze[x][y] not in ('S', 'E'):
            maze[x][y] = 'w' #way
    
for row in maze:
    print (' '.join(row))

print(len(shortest)-1)
