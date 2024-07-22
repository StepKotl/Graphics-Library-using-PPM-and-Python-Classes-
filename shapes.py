if __name__ == "__main__":
    import main
    main    

# ------------------------------------------- General Shape Class -------------------------------------------
class shape:
    def __init__(self, location : tuple, thickness : int = 1, colour : list = [0,0,0]):
        self.location = location
        self.coords = []
        self.colour = colour
        self.thickness = thickness

        # Generate the coordinates and scale as provided
        self.setCoordinates()
        self.scale(thickness)

    # Adds 2 tuples together
    def addTuple(self, tuple1 : tuple, tuple2 : tuple, extraDist : int = 0):
        return tuple([tuple1[0] + tuple2[0] + extraDist, tuple1[1] + tuple2[1]])

    # Multiplies a tuple by a set multiplier
    def multiplyTuple(self, tup : tuple, mulitplier : int):
        return tuple([tup[0] * mulitplier, tup[1] * mulitplier])

    # Defined depending on a given shape
    def setCoordinates(self):
        pass

    # Scales different depending on the shape
    def scale(self, scaleval):
        print("No Scale Funtion")

# ------------------------------------------- Text Class -------------------------------------------

class text(shape):
    def __init__(self, location : tuple,  thickness : int = 1, colour : list = [0,0,0], text : str = "Hello World"):
        
        # Shape Specific Classifications
        self.text = text
        self.importLetters()
        
        # Shape Class Super initialize
        super().__init__(location, thickness, colour)
    

    # Generates coordinates by taking the letters in the text, then adding those to the set location by the specific instance of the function
    def setCoordinates(self):
        distance = 0
        for character in self.text:
            size, points = self.letters[character.upper()]
            for point in points:
                PointColoured = self.addTuple(self.location, point, distance)
                self.coords.append(PointColoured)
            distance += size[0] + 1
        
        self.size = self.multiplyTuple((5, distance - 1), self.thickness)

    # Takes the pickeled letters and each of their coordinates (see pickling.py)
    def importLetters(self):
        import pickle
        
        with open("letters.pkl", "rb") as picklefile:
            letters = pickle.load(picklefile)

        self.letters = letters

    # muliplies all of the coordinated by a value to be scaled by (each point defines the new top right of the scaled square)
    # then fills between the new topright location and the negative scale value in either direction
    def scale(self, scaleval : int):
        newCoords = []
        for coord in self.coords:
            topRight = self.multiplyTuple(coord, scaleval)
            for x in range(scaleval):
                for y in range(scaleval):
                    newCoords.append(self.addTuple(topRight, (- x - (self.location[0] - 1) * (scaleval - 1), - y - (self.location[1] - 1) * (scaleval - 1))))
        self.coords = newCoords

    def wrap(self, gap : int, thickness : int, colour : list, boxyness : int = 1):
        radius = int(self.size[0] / 2 + gap)
        self.border = circle((self.addTuple(self.location, (- gap, - gap))), thickness, colour,  radius, (self.size[1] / 2 + gap) / radius, 1, boxyness)
        return self.border

# ------------------------------------------- Square Class -------------------------------------------

class square(shape):
    def __init__(self, location : tuple,  thickness : int = 1, colour : list = [0,0,0],  size : tuple = (0,0), filled : bool = False):
        self.filled = filled
        self.size = size
        super().__init__(location, thickness, colour)
        

    def setCoordinates(self):

        # if the square if filled, then fill in all of the values between the anchor location and the size of the square
        if self.filled:
            for y in range(self.size[1]):
                for x in range(self.size[0]):
                    self.coords.append(self.addTuple(self.location, (x,y)))
        else:
        
        # if not filled, then fill the lines from the location and the size points (0,0), (0,y), (x,0), (x,y)
            for y in range(self.size[1]):
                self.coords.append(self.addTuple(self.location, (0,y)))
                self.coords.append(self.addTuple(self.location, (self.size[0], y)))
            
            for x in range(self.size[0]):
                self.coords.append(self.addTuple(self.location, (x, 0)))
                self.coords.append(self.addTuple(self.location, (x, self.size[1])))
            self.coords.append(self.addTuple(self.location, (self.size[0], self.size[1])))
    
        # Create another square (scalar value) times that is 1 less in either corner
    def scale(self, scaleval):
        for level in range(1, scaleval):
            self.coords += square(self.addTuple((level - 1, level - 1), self.location), 1, self.colour, self.addTuple(self.size, (- (scaleval - 1), - (scaleval - 1))), self.filled).coords

# ------------------------------------------- Circle Class -------------------------------------------

class circle(shape):
    def __init__(self, location: tuple, thickness : int = 1, colour: list = [0, 0, 0], radius : int = 1, xScale : int = 1, yScale : int = 1, boxyness : int = 1):
        self.radius = radius
        self.xScale = xScale
        self.yScale = yScale
        self.boxyness = 2 * boxyness

        super().__init__(location, thickness, colour)


    def setCoordinates(self):
        
        for x in range(int(round(2 * self.radius * self.xScale + 1))):
            
            discriminant = (self.radius ** self.boxyness - (x / self.xScale - self.radius) ** self.boxyness)
            if discriminant < 0:
                print("Circle generation stopped")
                break
            y1 = int(round(self.yScale * (discriminant ** (1 / self.boxyness) + self.radius)))
            y2 = int(round(self.yScale * (- discriminant ** (1 / self.boxyness) + self.radius)))

            self.coords += [self.addTuple(self.location, (x, y1)), self.addTuple(self.location, (x, y2))]
        
        for y in range(int(round(2 * self.radius * self.yScale + 1))):
            
            discriminant = (self.radius ** self.boxyness - (y / self.yScale - self.radius) ** self.boxyness)
            if discriminant < 0:
                print("Circle generation stopped")
                break

            x1 = int(round(self.xScale * (discriminant ** (1 / self.boxyness) + self.radius)))
            x2 = int(round(self.xScale * (-discriminant ** (1 / self.boxyness) + self.radius)))

            self.coords += [self.addTuple(self.location, (x1, y)), self.addTuple(self.location, (x2, y))]
