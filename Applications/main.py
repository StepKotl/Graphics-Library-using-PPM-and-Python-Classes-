from ..Classes.Frame import frame
from ..Classes.Shapes import square, text, circle

bigScale = 30
smallScale = int(bigScale / 2)
textSize = 6
writtenText = ":3"
thing = frame((1920, 1080), [251, 219, 255])

bigFace = text((960 - int(textSize * bigScale), 540 - int((5 * bigScale) / 2)), bigScale, [226, 117, 250], writtenText)
smallFace = text((960 + int(textSize * smallScale), 540 - int((5 * smallScale) / 2)), smallScale, [226, 117, 250], writtenText)
border = square((0, 0), 3, [226, 117, 250], (1919, 1079), False)
bigFace.wrap(10, 1, smallFace.colour, 8)
smallFace.wrap(10, 1, smallFace.colour, 8)


lines = [bigFace, smallFace, border, bigFace.border, smallFace.border]

print("Shapes Placed")

thing.draw(lines)
print("Done")
