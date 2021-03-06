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
            y = int(round(startPoint[1] * (1 - t) + finishPoint[1] * t))
            image.set(x, y, color)

    def line3(self, startPoint, finishPoint, image, color):  # Вариант 3
        steep = False
        if math.fabs(startPoint[0] - finishPoint[0]) < math.fabs(startPoint[1] - finishPoint[1]):
            startPoint = (startPoint[1], startPoint[0])
            finishPoint = (finishPoint[1], finishPoint[0])
            steep = True
        if startPoint[0] > finishPoint[0]:
            startPoint, finishPoint = finishPoint, startPoint
        for x in range(startPoint[0], finishPoint[0]):
            t = (x - startPoint[0]) / (finishPoint[0] - startPoint[0])
            y = int(round(startPoint[1] * (1 - t) + finishPoint[1] * t))
            if steep:
                image.set(y, x, color)
            else:
                image.set(x, y, color)

    def line4(self, startPoint, finishPoint, image, color):  # Вариант 4. Брезенхем
        steep = False
        if math.fabs(startPoint[0] - finishPoint[0]) < math.fabs(startPoint[1] - finishPoint[1]):
            startPoint = (startPoint[1], startPoint[0])
            finishPoint = (finishPoint[1], finishPoint[0])
            steep = True

        if startPoint[0] > finishPoint[0]:
            startPoint, finishPoint = finishPoint, startPoint

        dx = -startPoint[0] + finishPoint[0]
        dy = -startPoint[1] + finishPoint[1]
        if dx == 0:
            derror = 0
        else:
            derror = math.fabs(dy / dx)
        error = 0
        y = startPoint[1]

        for x in range(startPoint[0], finishPoint[0]):
            if steep:
                image.set(y, x, color)
            else:
                image.set(x, y, color)
            error += derror
            if error > 0.5:
                if startPoint[1] > finishPoint[1]:
                    y += -1
                else:
                    y += 1
                error -= 1

    def drawPolygon(self, model, polygon, image, color, use_z_buffer):
        point0 = model.points[polygon[0] - 1]
        point1 = model.points[polygon[1] - 1]
        point2 = model.points[polygon[2] - 1]

        cords0 = model.cords[polygon[0] - 1]
        cords1 = model.cords[polygon[1] - 1]
        cords2 = model.cords[polygon[2] - 1]

        xmin = min(point0[0], point1[0], point2[0])
        xmax = max(point0[0], point1[0], point2[0])
        if (xmin < 0 and xmax < 0) or (xmin >= image.width and xmax >= image.width):
            return
        if (xmin < 0):
                xmin = 0
        if (xmax < 0):
            xmax = 0
        if (xmax >= image.width):
            xmax = image.width - 1
        if (xmin >= image.width):
            xmin = image.width - 1
        ymin = min(point0[1], point1[1], point2[1])
        ymax = max(point0[1], point1[1], point2[1])
        if (ymin < 0 and ymax < 0) or (ymin >= image.height and ymax >= image.height):
            return
        if (ymin < 0):
            ymin = 0
        if (ymax < 0):
            ymax = 0
        if (ymax >= image.height):
            ymax = image.height - 1
        if (ymin >= image.height):
            ymin = image.height - 1

        p = 1

        for x in range(xmin, xmax+1):
            for y in range(ymin, ymax+1):
                bar_coef = model.getBaricentCords((x, y), polygon)
                if bar_coef[0] > 0 and bar_coef[1] > 0 and bar_coef[2] > 0:
                    if use_z_buffer:
                        z = bar_coef[0]*cords0[2] + bar_coef[1]*cords1[2] + bar_coef[2]*cords2[2]
                        if z > image.getZ(x, y):
                            image.set(x, y, color)
                            image.setZ(x, y, z)
                    else:
                        image.set(x, y, color)

    def calclight(self, l, n0, n1, n2, bar_cords):
        norm_l = math.sqrt(math.pow(l[0], 2) + math.pow(l[1], 2) + math.pow(l[2], 2))
        norm_n0 = math.sqrt(math.pow(n0[0], 2) + math.pow(n0[1], 2) + math.pow(n0[2], 2))
        norm_n1 = math.sqrt(math.pow(n1[0], 2) + math.pow(n1[1], 2) + math.pow(n1[2], 2))
        norm_n2 = math.sqrt(math.pow(n2[0], 2) + math.pow(n2[1], 2) + math.pow(n2[2], 2))
        l0 = (n0[0] * l[0] + n0[1] * l[1] + n0[2] * l[2]) / (norm_l * norm_n0)
        l1 = (n1[0] * l[0] + n1[1] * l[1] + n1[2] * l[2]) / (norm_l * norm_n1)
        l2 = (n2[0] * l[0] + n2[1] * l[1] + n2[2] * l[2]) / (norm_l * norm_n2)

        light = 255 * (bar_cords[0] * l0 + bar_cords[1] * l1 + bar_cords[2] * l2)

        return light

    def drawPolygon_Guro(self, model, polygon, apex_norm, image):
        point0 = model.points[polygon[0] - 1]
        point1 = model.points[polygon[1] - 1]
        point2 = model.points[polygon[2] - 1]

        cords0 = model.cords[polygon[0] - 1]
        cords1 = model.cords[polygon[1] - 1]
        cords2 = model.cords[polygon[2] - 1]

        xmin = min(point0[0], point1[0], point2[0])
        xmax = max(point0[0], point1[0], point2[0])
        if (xmin < 0 and xmax < 0) or (xmin >= image.width and xmax >= image.width):
            return
        if (xmin < 0):
            xmin = 0
        if (xmax < 0):
            xmax = 0
        if (xmax >= image.width):
            xmax = image.width - 1
        if (xmin >= image.width):
            xmin = image.width - 1
        ymin = min(point0[1], point1[1], point2[1])
        ymax = max(point0[1], point1[1], point2[1])
        if (ymin < 0 and ymax < 0) or (ymin >= image.height and ymax >= image.height):
            return
        if (ymin < 0):
            xmin = 0
        if (ymax < 0):
            ymax = 0
        if (ymax >= image.height):
            ymax = image.height - 1
        if (ymin >= image.height):
            ymin = image.height - 1

        l = model.light

        n0 = model.vect_normals[apex_norm[0] - 1]
        n1 = model.vect_normals[apex_norm[1] - 1]
        n2 = model.vect_normals[apex_norm[2] - 1]

        for x in range(xmin, xmax + 1):
            for y in range(ymin, ymax + 1):
                bar_coef = model.getBaricentCords((x, y), polygon)
                if bar_coef[0] > 0 and bar_coef[1] > 0 and bar_coef[2] > 0:
                    z = bar_coef[0] * cords0[2] + bar_coef[1] * cords1[2] + bar_coef[2] * cords2[2]
                    if z > image.getZ(x, y):
                        color = int(self.calclight(l, n0, n1, n2, bar_coef))
                        image.set(x, y, (color, color, color))
                        image.setZ(x, y, z)



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
image.save('Output/Task3_Line1.jpg')

image = MyImage(200, 200)
for finishPoint in finishPoints:
    drawer.line1(startPoint, finishPoint, image, (255, 255, 255), 0.1)
image.save('Output/Task3_Line2.jpg')

image = MyImage(200, 200)
for finishPoint in finishPoints:
    drawer.line2(startPoint, finishPoint, image, (255, 255, 255))
image.save('Output/Task3_Line3.jpg')

image = MyImage(200, 200)
for finishPoint in finishPoints:
    drawer.line3(startPoint, finishPoint, image, (255, 255, 255))
image.save('Output/Task3_Line4.jpg')

image = MyImage(200, 200)
for finishPoint in finishPoints:
    drawer.line4(startPoint, finishPoint, image, (255, 255, 255))
image.save('Output/Task3_Line5.jpg')
