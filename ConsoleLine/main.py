import time
import matplotlib.pyplot as plt
from matplotlib.pyplot import imshow
from PIL import Image, ImageDraw
import numpy as np
import pygame

# Функция для рисования отрезка с помощью алгоритма Брезенхема
def draw_line_bresenham(img, x0, y0, x1, y1, color):
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    err = dx - dy

    while True:
        img.putpixel((x0, y0), color)
        if x0 == x1 and y0 == y1:
            break
        e2 = err * 2
        if e2 > -dy:
            err -= dy
            x0 += sx
        if e2 < dx:
            err += dx
            y0 += sy

# Функция для замера времени рисования с помощью Брезенхема
def measure_bresenham(x0, y0, x1, y1, color):
    img = Image.new('RGB', (1000, 900), 'white')
    start_time = time.perf_counter()  # Используем более точный таймер
    draw_line_bresenham(img, x0, y0, x1, y1, color)
    end_time = time.perf_counter()
    return end_time - start_time

# Функция для замера времени рисования с помощью Pygame
def measure_pygame(x0, y0, x1, y1, color):
    screen = pygame.Surface((1000, 900))  # Создаем поверхность
    start_time = time.perf_counter()  # Используем более точный таймер
    pygame.draw.line(screen, color, (x0, y0), (x1, y1))
    end_time = time.perf_counter()
    return end_time - start_time

# Инициализируем Pygame один раз
pygame.init()

# Координаты для тестирования
x0, y0 = 50, 50
x1, y1 = 950, 850
color = (0, 0, 0)  # Чёрный цвет

# Замер времени для каждого метода
bresenham_time = measure_bresenham(x0, y0, x1, y1, color)
pygame_time = measure_pygame(x0, y0, x1, y1, color)

# Выводим результаты
print(f"Время выполнения алгоритма Брезенхема: {bresenham_time:.6f} секунд")
print(f"Время выполнения pygame.draw.line: {pygame_time:.6f} секунд")

# Визуализация результата с несколькими цветными линиями
img = Image.new('RGB', (1000, 900), 'white')
draw = ImageDraw.Draw(img)

# Рисуем несколько линий по Брбрбрбрбрезенхему и по pygame'у
draw_line_bresenham(img, x0, y0, x1, y1, color)
draw.line((500, 50, 500, 850), fill=(0, 0, 0), width=2)    # Черная вертикальная линия

# Отображение изображения с помощью matplotlib
imshow(np.asarray(img))
plt.show()

# Сохранение изображения
img.save('Visualized_Lines_not.png')

# Закрываем Pygame после всех замеров
pygame.quit()