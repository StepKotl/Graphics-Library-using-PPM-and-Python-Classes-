class shape:
    def __init__(self, location : tuple, thickness : int = 1, colour : list = [0,0,0]):
        self.location = location
        self.coords = []
        self.colour = colour
        self.setCoordinates()
        self.scale(thickness)
    
    def addTuple(self, tuple1 : tuple, tuple2 : tuple, extraDist : int = 0):
        return tuple([tuple1[0] + tuple2[0] + extraDist, tuple1[1] + tuple2[1]])
    
    def multiplyTuple(self, tup : tuple, mulitplier : int):
        return tuple([tup[0] * mulitplier, tup[1] * mulitplier])
    
    def setCoordinates(self):
        pass

    def scale(self, scaleval):
        print("No Scale Funtion")


class text(shape):
    def __init__(self, location : tuple,  thickness : int = 1, colour : list = [0,0,0], text : str = "Hello World"):
        self.text = text
        self.importLetters()
        
        super().__init__(location, thickness, colour)
    
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
    
    def scale(self, scaleval : int):
        newCoords = []
        for coord in self.coords:
            topRight = self.multiplyTuple(coord, scaleval)
            for x in range(scaleval):
                for y in range(scaleval):
                    newCoords.append(self.addTuple(topRight, (- x - (self.location[0] - 1) * (scaleval - 1), - y - (self.location[1] - 1) * (scaleval - 1))))
        self.coords = newCoords



class square(shape):
    def __init__(self, location : tuple,  thickness : int = 1, colour : list = [0,0,0],  size : tuple = (0,0), filled : bool = False):
        self.filled = filled
        self.size = size
        super().__init__(location, thickness, colour)
        

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
    
    def scale(self, scaleval):
        for level in range(1, scaleval):
            self.coords += square(self.addTuple((level, level), self.location), 1, self.colour, self.addTuple(self.size, (-scaleval, -scaleval)), self.filled).coords


class circle(shape):
    def __init__(self, location: tuple, thickness : int = 1, colour: list = [0, 0, 0], radius : int = 1, xScale : int = 1, yScale : int = 1, boxyness : int = 1):
        self.radius = radius
        self.xScale = xScale
        self.yScale = yScale
        self.boxyness = boxyness

        super().__init__(location, thickness, colour)

    def setCoordinates(self):
        
        for x in range(int(round(2 * self.radius * self.xScale))):
            pass