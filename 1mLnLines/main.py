import time
import random
import pygame
import math

# Инициализация Pygame
pygame.init()
screen = pygame.Surface((1000, 1000))

# Функция алгоритма Брезенхема
def bresenham_line(x1, y1, x2, y2):
    points = []
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1
    err = dx - dy

    while True:
        points.append((x1, y1))
        if x1 == x2 and y1 == y2:
            break
        e2 = err * 2
        if e2 > -dy:
            err -= dy
            x1 += sx
        if e2 < dx:
            err += dx
            y1 += sy
    return points

# Генерация случайных отрезков
num_lines = 1000000
segments = [(random.randint(0, 999), random.randint(0, 999), random.randint(0, 999), random.randint(0, 999)) for _ in range(num_lines)]

# Замер для алгоритма Брезенхема
total_bresenham_pixels = 0
start_time = time.time()
for x1, y1, x2, y2 in segments:
    points = bresenham_line(x1, y1, x2, y2)
    total_bresenham_pixels += len(points)
end_time = time.time()
bresenham_time = end_time - start_time
bresenham_density = total_bresenham_pixels / bresenham_time
print("Время выполнения алгоритма Брезенхема:", bresenham_time)
print("Плотность отрисовки для алгоритма Брезенхема (пиксели/сек):", bresenham_density) # ну я больше ничего не придумал :(
# Пояснения
# Алгоритм Брезенхема строит линию, добавляя каждый пиксель, через который проходит линия, в список points
# Длина списка - количество пикселей


# Замер для метода Pygame
total_pygame_pixels = 0
start_time = time.time()
for x1, y1, x2, y2 in segments:
    pygame.draw.line(screen, (255, 255, 255), (x1, y1), (x2, y2))
    # Приближение числа пикселей для Pygame через длину отрезка
    total_pygame_pixels += abs(math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2))
end_time = time.time()
pygame_time = end_time - start_time
pygame_density = total_pygame_pixels / pygame_time
print("Время выполнения метода Pygame:", pygame_time)
print("Плотность отрисовки для метода Pygame (пиксели/сек):", pygame_density)
# Пояснения
# Метод pygame.draw.line() рисует линию, но не возвращает информацию о конкретных пикселях, через которые проходит линия.
# Чтобы приблизительно оценить число пикселей, мы используем abs(math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2))
# Под корнем просто формула длины отрезка: <<c^2 = a^2 + b^2>>


# Завершение Pygame
pygame.quit()