import random
import time
import numpy as np

def generate(vertices, edges):
    a = np.zeros((vertices, vertices), dtype=np.int32)
    for i in range(edges):
        found = False
        while not found:
            x = random.randrange(0, vertices, 1)
            y = random.randrange(0, vertices, 1)
            if x != y and a[x][y] != 1:
                a[x][y] = 1
                a[y][x] = 1
                found = True
    return a

def find(i, p):
    global timer
    timer = timer + 1
    upMatrix[0][i] = timer
    tinMatrix[0][i] = timer
    visited[0][i] = 1
    children = 0

    for j in range(vert):
            if j == p:
                continue
            if visited[0][j] == 1:
                if matrix[i][j] == 1:
                    upMatrix[0][i] = min(upMatrix[0][i], tinMatrix[0][j])
            else:
                if matrix[i][j] == 1:
                    find(j, i)
                    children = children + 1
                    upMatrix[0][i] = min(upMatrix[0][i], upMatrix[0][j])
                    if p != -1 and upMatrix[0][j] >= tinMatrix[0][i]:
                          points.append(i)
    if p == -1 and children >= 2:
        points.append(i)


#Запрашиваем входные данные у пользователя. Для тестов производился следующий цикл:
# for i in range(2, 201, 1):
#     vert = i
#     edg = random.randrange(1, vert * (vert - 1) / 2 + 1, 1)
#     ...

vert = input ('Ввердите число вершин: ')
edg = input ('Ввердите число ребер: ')
vert = int(vert)
edg = int(edg)

#Массив для искомых точек
points = []
timer = 0

visited = np.zeros((1, vert), dtype=np.int32)
tinMatrix = np.zeros((1, vert), dtype=np.int32)
upMatrix = np.zeros((1, vert), dtype=np.int32)

#Генерация матрицы смежности
matrix = generate(vert, edg)
print(matrix)

#Засекаем время после генерирования входных данных
start_time = time.time()
for s in range(vert):
    if visited[0][s] != 1:
        find(s, -1)

#Выводим результаты
print('Затраченное время: ', time.time() - start_time)
print('Точки сочленения: ', points)
