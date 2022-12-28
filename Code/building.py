
class Building:
    def __init__(self, w=1, h=1, img=None, woodCost=0, goldCost=0, manaCost=0):
        self.w = w
        self.h = h
        self.img = img
        self.woodCost = woodCost
        self.goldCost = goldCost
        self.manaCost = manaCost

    def getSize(self):
        return self.w, self.h 
