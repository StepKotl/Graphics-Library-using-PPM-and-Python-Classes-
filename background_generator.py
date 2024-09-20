from drawing import frame
from shapes import square, text, circle
import math

scale = 17
textSize = 35
writtenText = "Step.Kotl"
thing = frame((720, 1600), [0, 0, 0])

Name = text((int(thing.size[0] / 2 - int((textSize * scale) / 2)), (int(thing.size[1] * 1/2) - int((5 * scale) / 2))), scale, [109, 204, 106], writtenText)
border = square((0, 0), 7, [77, 161, 74], (thing.size[0] - 1, thing.size[1] - 1), False)

lines = []

for x in range(int(math.floor((thing.size[0]) / (textSize + 2))) + 1):
    for y in range(int((thing.size[1]) / 6)):
        lines += [text(((textSize + 2) * x, 6 * y), 1, [42, 77, 41], writtenText)]


lines += [Name, border]

print("Shapes Placed")

thing.draw(lines)
print("Done")