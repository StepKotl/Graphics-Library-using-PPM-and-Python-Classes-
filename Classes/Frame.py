if __name__ == "__main__":
    pass

from Shapes import shape

class frame ():
    def __init__(self, size : tuple, background : list = [254, 254, 254]):
        self.size = size        
        self.colourmat = [[background for i in range(size[0])] for i in range(size[1])]
        self.placementmat = [[False for i in range(size[0])] for i in range(size[1])]

    def setToMat(self, point : tuple, colour : list):
        self.colourmat[- point[1] - 1][point[0]] = colour
        self.placementmat[point[1]][point[0]] = True

    def draw(self, shapes : list):
        for figure in shapes:

            for coord in figure.coords:
                try:
                    self.setToMat(coord, figure.colour)

                except IndexError:
                    print(f"Could not place {coord} in frame")

        settings = f"P3 \n{self.size[0]} {self.size[1]}\n255\n"

        out = ""        
        for row in self.colourmat:
            for colour in row:
                out += f"{colour[0]} {colour[1]} {colour[2]}\n"

        with open("picture.ppm", "wb+") as colouringbook:
            colouringbook.write((settings + out).encode("ascii"))

