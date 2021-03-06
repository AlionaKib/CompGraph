from PIL import Image, ImageDraw
import numpy as np


class MyImage:

    def __init__(self, width, height):
        self.image_arr = np.zeros((width, height), dtype=tuple)
        self.height = height
        self.width = width
        self.size = self.image_arr.shape
        self.z_buffer = np.zeros((width, height), dtype=float)
        for x in range(width):
            for y in range(height):
                self.image_arr[x, y] = (0, 0, 0)
                self.z_buffer[x, y] = -100

    def loadImage(self, imageName):
        image = Image.open(imageName)  # Открываем изображение
        self.size = image.size
        self.width = image.size[0]  # Определяем ширину
        self.height = image.size[1]  # Определяем высоту
        self.image_arr = image.load()  # Выгружаем значения пикселей

    def set(self, x, y, value):
        if x < self.height and y < self.width and x >= 0 and y >=0:
            self.image_arr[x, y] = value

    def setZ(self, x, y, z):
        if x < self.height and y < self.width and x >= 0 and y >= 0:
            self.z_buffer[x, y] = z

    def getZ(self, x, y):
        return self.z_buffer[x, y]


    def get(self, x, y):
        return self.image_arr[x, y]

    def save(self, imageName):
        image = Image.new("RGB", self.size)  # Создаем изображение. L - 8 бит, черно-белое
        draw = ImageDraw.Draw(image)  # Создаем инструмент для рисования

        for x in range(self.width):
            for y in range(self.height):
                draw.point((x, y), self.image_arr[x, y])  # рисуем пиксель

        image.save(imageName, "JPEG")  # не забываем сохранить изображение

"""
image = MyImage(100, 100)
image.loadImage('Output/Task1_Multicolor.jpg')
print(image.get(100, 100))
for i in range(50, 100):
    for j in range(50, 100):
        image.set(i, j, (255, 0, 0))

image.save('Output/Task2_MyImageTest.jpg')
"""
