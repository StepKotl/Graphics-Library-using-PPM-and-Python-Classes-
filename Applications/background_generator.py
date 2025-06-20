import os

from ..Classes.Frame import frame
from ..Classes.Shapes import square, text, circle
import math


# Define some constants and the frame
scale = 17
textSize = 35
writtenText = "Step.Kotl"
thing = frame((720, 1600), [0, 0, 0])

# Create the larger text, centered using the defined constants
Name = text((int(thing.size[0] / 2 - int((textSize * scale) / 2)), (int(thing.size[1] * 1/2) - int((5 * scale) / 2))), scale, [109, 204, 106], writtenText)

# Create the squre border, again based on above constants
border = square((0, 0), 7, [77, 161, 74], (thing.size[0] - 1, thing.size[1] - 1), False)

lines = []

# Generate the smaller text in the background
for x in range(int(math.floor((thing.size[0]) / (textSize + 2))) + 1):
    for y in range(int((thing.size[1]) / 6)):
        lines += [text(((textSize + 2) * x, 6 * y), 1, [42, 77, 41], writtenText)]
    # for
# for       


# add the other two shapes, and draw the image
lines += [Name, border]

print("Shapes Placed")

thing.draw(lines)
print("Done")