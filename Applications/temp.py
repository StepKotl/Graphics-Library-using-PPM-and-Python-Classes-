from ..Classes.frame import Frame
from ..Classes.Shapes import *

background = Frame((1080, 1920), [245, 66, 191])

objects = []

scale = 220

objects.append(circle((0,0), 1, (88, 233, 252), scale, 1, 1, 1))
objects.append(circle((scale * 2,0), 1, (88, 233, 252), scale, 1, 1, 1))
objects.append(circle((scale, int(scale * 2 - (scale / 2.4))), 1, (88, 233, 252), scale, 1, 3, 1))
objects.append(text(()))

background.draw(objects)




