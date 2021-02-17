from Task2 import MyImage
import numpy as np
import math as math

class Drawer:
    def swap(self, x, y):
        t = x
        x = y
        y = t


    def line1(self, startPoint, finishPoint, image, color, dt):  # Простейшая прямая
        t = 0
        while t < 1:
            x = int(startPoint[0] * (1 - t) + finishPoint[0] * t)
            y = int(startPoint[1] * (1 - t) + finishPoint[1] * t)
            image.set(x, y, color)
            t += dt


    def line2(self, startPoint, finishPoint, image, color):  # Вариант 2
        for x in range(startPoint[0], finishPoint[0]):
            t = (x - startPoint[0]) / (finishPoint[0] - startPoint[0])
            y = int(startPoint[1] * (1 - t) + finishPoint[1] * t)
            image.set(x, y, color)


    def line3(self, startPoint, finishPoint, image, color):  # Вариант 3
        steep = False
        if math.fabs(startPoint[0] - finishPoint[0]) < math.fabs(startPoint[1] - finishPoint[1]):
            self.swap(startPoint[0], startPoint[1])
            self.swap(finishPoint[0], finishPoint[1])
            self.steep = True
        if startPoint[0] > finishPoint[0]:
            self.swap(startPoint[0], finishPoint[0])
            self.swap(startPoint[1], finishPoint[1])
        for x in range(startPoint[0], finishPoint[0]):
            t = (x - startPoint[0]) / (finishPoint[0] - startPoint[0])
            y = int(startPoint[1] * (1 - t) + finishPoint[1] * t)
            if steep:
                image.set(y, x, color)
            else:
                image.set(x, y, color)

drawer = Drawer()

startPoint = (100, 100)
finishPoints = np.zeros(13, dtype=tuple)

for k in range(0, 13):
    alpha = 2 * math.pi * k / 13
    x = int(100 + 95 * math.cos(alpha))
    y = int(100 + 95 * math.sin(alpha))
    finishPoints[k] = (x, y)

image = MyImage(200, 200)
for finishPoint in finishPoints:
    drawer.line1(startPoint, finishPoint, image, (255, 255, 255), 0.01)
image.save('Task3_Line1.jpg')

image = MyImage(200, 200)
for finishPoint in finishPoints:
    drawer.line1(startPoint, finishPoint, image, (255, 255, 255), 0.1)
image.save('Task3_Line2.jpg')

image = MyImage(200, 200)
for finishPoint in finishPoints:
    drawer.line2(startPoint, finishPoint, image, (255, 255, 255))
image.save('Task3_Line3.jpg')

image = MyImage(200, 200)
for finishPoint in finishPoints:
    drawer.line3(startPoint, finishPoint, image, (255, 255, 255))
image.save('Task3_Line4.jpg')
