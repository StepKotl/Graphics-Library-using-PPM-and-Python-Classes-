from drawing import frame
from shapes import square, text

thing = frame((81, 81), [251, 219, 255])

lines = []
for x in range(10):
    for y in range(10):
        textLine = text((8 * x + 2, 2 + y * 8), [0, 0, 0], ":3")
        box = square((8, 8), (8 * x, y * 8), [0, 0, 0], False)
        lines += [textLine, box]





thing.draw(lines)
pass