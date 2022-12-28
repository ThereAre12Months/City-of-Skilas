# LWorld -> limited world (maximum world size)
class LWorld:
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.genWorld()

    def genWorld(self):
        self.matrix = []
        for x in range(self.w):
            self.matrix.append([])
            for y in range(self.h):
                self.matrix[-1].append(None)

    def place(self, b, x, y): # b = building
        w, h = b.getSize()

        for i in range(w):
            for j in range(h):
                self.matrix[i+x][j+y] = [x, y]

    def getBuilding(self, x, y):
        b = self.matrix[x][y]
        if type(b) == list:
            b = self.matrix[b[0]][b[1]]
        return b

    def remove(self, x, y):
        b = self.matrix[x][y]
        if type(b) == list:
            x, y = b
            b = self.matrix[b[0]][b[1]]
        elif b == None:
            return

        w, h = b.getSize()
        for i in range(w):
            for j in range(h):
                self.matrix[i+x][j+y] = None

    def getBuildingsInRange(self, x, y, w, h):
        buildings = {}
        for i in range(w):
            for j in range(h):
                b = self.matrix[i+x][j+y]
                if b == None:
                    pass
                elif type(b) == list:
                    if not b in buildings.keys():
                        x2, y2 = b
                        b = self.matrix[x2][y2]
                        buildings.update({[x2, y2]:b})
                else:
                    buildings.update({[i+x,j+y]:b})
            return buildings
