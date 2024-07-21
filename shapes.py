class shape:
    def __init__(self, size : tuple, location : tuple, colour : list = [0,0,0]):
        self.size = size
        self.location = location
        self.coords = []
        self.colour = colour
        self.setCoordinates()
    
    def addTuple(self, tuple1, tuple2, extraDist = 0):
        return tuple([tuple1[0] + tuple2[0] + extraDist, tuple1[1] + tuple2[1]])
    
    def multiplyTuple(self, tup, mulitplier):
        return tuple([tup[0] * mulitplier, tup[1] * mulitplier])
    
    def setCoordinates(self):
        pass

    def scale(self, scaleval):
        newCoords = []
        for coord in self.coords:
            topRight = self.multiplyTuple(coord, scaleval)
            for x in range(scaleval):
                for y in range(scaleval):
                    newCoords.append(self.addTuple(topRight, (-x, -y)))
        self.coords = newCoords            


class text(shape):
    def __init__(self, location : tuple, colour : list, text : str):
        self.text = text
        self.importLetters()

        # Code doesn't function without this line for some reason :3 don't delete
        size = 0
        
        super().__init__(size, location, colour)
    
    def setCoordinates(self):
        distance = 0
        for character in self.text:
            size, points = self.letters[character.upper()]
            for point in points:
                PointColoured = self.addTuple(self.location, point, distance)
                self.coords.append(PointColoured)
            distance += size[0] + 1

    def importLetters(self):
        import pickle
        
        with open("letters.pkl", "rb") as picklefile:
            letters = pickle.load(picklefile)

        self.letters = letters



class square(shape):
    def __init__(self, size : tuple, location : tuple, colour : list, filled : bool = False):
        self.filled = filled
        super().__init__(size, location, colour)
        

    def setCoordinates(self):
        if self.filled:
            for y in range(self.size[1]):
                for x in range(self.size[0]):
                    self.coords.append(self.addTuple(self.location, (x,y)))
        else:
            for y in range(self.size[1]):
                self.coords.append(self.addTuple(self.location, (0,y)))
                self.coords.append(self.addTuple(self.location, (self.size[0], y)))
            
            for x in range(self.size[0]):
                self.coords.append(self.addTuple(self.location, (x, 0)))
                self.coords.append(self.addTuple(self.location, (x, self.size[1])))
            self.coords.append(self.addTuple(self.location, (self.size[0], self.size[1])))
