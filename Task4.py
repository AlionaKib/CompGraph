import re

class Model:
    def __init__(self):
        self.cords = []
        self.poligons = []

    def load(self, fileName, polygonsNumber):
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
        f.close()

    def getCords(self):
        return self.cords

    def getPoligons(self):
        return self.poligons