import re
import math
import numpy as np


class Model:
    def __init__(self):
        self.cords = []
        self.poligons = []
        self.points = []
        self.cords_scale = []
        self.normals = []
        self.cos_light = []
        self.ax = 1
        self.ay = 1
        self.u0 = 0
        self.v0 = 0

    def load(self, fileName, polygonsNumber, light):
        f = open(fileName)
        self.cords.clear()
        self.poligons.clear()
        for line in f:
            s = line
            if len(s) > 0 and (s[0] == 'v') and (s[1] == ' '):
                t = ()
                nums = re.findall(r'[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?', s)
                nums = [float(i) for i in nums]
                t = (nums[0], nums[1], nums[2])
                self.cords.append(t)
            if len(s) > 0 and (s[0] == 'f') and (s[1] == ' '):
                t = ()
                nums = re.findall(r'\d+', s)
                nums = [int(i) for i in nums]
                t = (nums[polygonsNumber[0]], nums[polygonsNumber[1]], nums[polygonsNumber[2]])
                self.poligons.append(t)

        for polygon in self.poligons:
            cords0 = self.cords[polygon[0] - 1]
            cords1 = self.cords[polygon[1] - 1]
            cords2 = self.cords[polygon[2] - 1]
            vec1 = (cords1[0] - cords0[0], cords1[1] - cords0[1], cords1[2] - cords0[2])
            vec2 = (cords1[0] - cords2[0], cords1[1] - cords2[1], cords1[2] - cords2[2])
            i_norm = vec1[1] * vec2[2] - vec1[2] * vec2[1]
            j_norm = -vec1[0] * vec2[2] - vec1[2] * vec2[0]
            k_norm = vec1[0] * vec2[1] - vec1[1] * vec2[0]
            norm = (i_norm, j_norm, k_norm)
            self.normals.append(norm)

            norm_l = math.sqrt(math.pow(light[0], 2) + math.pow(light[1], 2) + math.pow(light[2], 2))
            norm_n = math.sqrt(math.pow(norm[0], 2) + math.pow(norm[1], 2) + math.pow(norm[2], 2))
            cos_light = (norm[0] * light[0] + norm[1] * light[1] + norm[2] * light[2]) / (norm_l * norm_n)
            self.cos_light.append(cos_light)

        f.close()

    def setScale(self, ax, ay, u0, v0):
        self.ax = ax
        self.ay = ay
        self.u0 = u0
        self.v0 = v0

    def changeScale(self):
        self.points.clear()
        self.cords_scale.clear()
        for cord in self.cords:
            # x_scale = ax * (cord[0] + t[0]) + u0 * cord[2]
            # y_scale = ay * (cord[1] + t[1]) + v0 * cord[2]
            x_scale = self.ax * cord[0] + self.u0
            y_scale = self.ay * cord[1] + self.v0
            x = int(x_scale)
            y = int(y_scale)
            point = (x, y)
            point_scale = (x_scale, y_scale)
            self.points.append(point)
            self.cords_scale.append(point_scale)

    def getCords(self):
        return self.cords

    def getPoligons(self):
        return self.poligons

    def getPoints(self):
        return self.points

    def getCos_light(self):
        return self.cos_light

    def getBaricentCords(self, point, polygon):
        cords0 = self.cords_scale[polygon[0] - 1]
        cords1 = self.cords_scale[polygon[1] - 1]
        cords2 = self.cords_scale[polygon[2] - 1]
        lambda0 = ((cords1[0] - cords2[0]) * (point[1] - cords2[1]) - (cords1[1] - cords2[1]) * (
                point[0] - cords2[0])) / \
                  ((cords1[0] - cords2[0]) * (cords0[1] - cords2[1]) - (cords1[1] - cords2[1]) * (
                          cords0[0] - cords2[0]))

        lambda1 = ((cords2[0] - cords0[0]) * (point[1] - cords0[1]) - (cords2[1] - cords0[1]) * (
                point[0] - cords0[0])) / \
                  ((cords2[0] - cords0[0]) * (cords1[1] - cords0[1]) - (cords2[1] - cords0[1]) * (
                          cords1[0] - cords0[0]))

        lambda2 = ((cords0[0] - cords1[0]) * (point[1] - cords1[1]) - (cords0[1] - cords1[1]) * (
                point[0] - cords1[0])) / \
                  ((cords0[0] - cords1[0]) * (cords2[1] - cords1[1]) - (cords0[1] - cords1[1]) * (
                          cords2[0] - cords1[0]))
        baricent_cords = (lambda0, lambda1, lambda2)
        return baricent_cords

    def rotate(self, alpha, betta, gamma):
        a = np.array([[1, 0, 0], [0, math.cos(alpha), math.sin(alpha)], [0, -math.sin(alpha), math.cos(alpha)]])
        b = np.array([[math.cos(betta), 0, math.sin(betta)], [0, 1, 0], [-math.sin(betta), 0, math.cos(betta)]])
        c = np.array([[math.cos(gamma), math.sin(gamma), 0], [-math.sin(gamma), math.cos(gamma), 0], [0, 0, 1]])

        r1 = a.dot(b)
        r = r1.dot(c)

        temp_cords = []

        for cord in self.cords:
            x = r[0, 0] * cord[0] + r[0, 1] * cord[1] + r[0, 2] * cord[2]
            y = r[1, 0] * cord[0] + r[1, 1] * cord[1] + r[1, 2] * cord[2]
            z = r[2, 0] * cord[0] + r[2, 1] * cord[1] + r[2, 2] * cord[2]
            new_cords = (x, y, z)
            temp_cords.append(new_cords)
        self.cords.clear()
        self.cords = temp_cords

        self.changeScale()