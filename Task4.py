import re


class Model:
    def __init__(self):
        self.cords = []
        self.poligons = []
        self.points = []
        self.cords_scale = []

    def load(self, fileName, polygonsNumber, xCoef, xdisp, yCoef, yDisp):
        f = open(fileName)
        self.cords.clear()
        self.poligons.clear()
        self.points.clear()
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
        for cord in self.cords:
            x_scale = xCoef * cord[0] + xdisp
            y_scale = yCoef * cord[1] + yDisp
            x = int(x_scale)
            y = int(y_scale)
            point = (x, y)
            point_scale = (x_scale, y_scale)
            self.points.append(point)
            self.cords_scale.append(point_scale)
        f.close()

    def getCords(self):
        return self.cords

    def getPoligons(self):
        return self.poligons

    def getPoints(self):
        return self.points

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
