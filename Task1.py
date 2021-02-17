from PIL import Image, ImageDraw
import numpy as np

H = 512
W = 512

pix = np.zeros((H, W), dtype=int)  # Матрица HxW заполненная нулями

size = pix.shape  # shape возвращает кортеж из ширины и высоты матрицы
image = Image.new("L", size)  # Создаем изображение. L - 8 бит, черно-белое
draw = ImageDraw.Draw(image)  # Создаем инструмент для рисования
width = size[0]
height = size[1]

for x in range(width):
    for y in range(height):
        g = int(255 * pix[x, y])
        draw.point((x, y), g)  # рисуем пиксель

image.save("resultBlack.jpg", "JPEG")  # не забываем сохранить изображение

pix = np.ones((H, W), dtype=int)  # Матрица HxW заполненная единицами

size = pix.shape  # shape возвращает кортеж из ширины и высоты матрицы
image = Image.new("L", size)  # Создаем изображение. L - 8 бит, черно-белое

draw = ImageDraw.Draw(image)  # Создаем инструмент для рисования
width = size[0]
height = size[1]

for x in range(width):
    for y in range(height):
        g = int(255 * pix[x, y])
        draw.point((x, y), g)  # рисуем пиксель

image.save("resultWhite.jpg", "JPEG")  # не забываем сохранить изображение

pix = np.ones((H, W), dtype=tuple)

size = pix.shape  # shape возвращает кортеж из ширины и высоты матрицы
image = Image.new("RGB", size)  # Создаем изображение. L - 8 бит, черно-белое

draw = ImageDraw.Draw(image)  # Создаем инструмент для рисования
width = size[0]
height = size[1]

for x in range(width):
    for y in range(height):
        pix[x, y] = (255, 0, 0)

for x in range(width):
    for y in range(height):
        g = pix[x, y]
        draw.point((x, y), g)  # рисуем пиксель

image.save("resultRed.jpg", "JPEG")  # не забываем сохранить изображение

pix = np.ones((H, W), dtype=tuple)

size = pix.shape  # shape возвращает кортеж из ширины и высоты матрицы
image = Image.new("RGB", size)  # Создаем изображение. L - 8 бит, черно-белое

draw = ImageDraw.Draw(image)  # Создаем инструмент для рисования
width = size[0]
height = size[1]

for x in range(width):
    for y in range(height):
        r = int(x * 255 / width)
        g = int(y * 255 / height)
        b = int((r + g) / 2)
        pix[x, y] = (r, g, b)

for x in range(width):
    for y in range(height):
        g = pix[x, y]
        draw.point((x, y), g)  # рисуем пиксель

image.save("resultRand.jpg", "JPEG")  # не забываем сохранить изображение
