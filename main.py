from drawing import frame
from shapes import square, text

bigScale = 30
smallScale = int(bigScale / 2)
textSize = 27
writtenText = "Stephan"
thing = frame((1920, 1080), [251, 219, 255])

bigFace = text((960 - int(textSize * bigScale), 540 - int((5 * bigScale) / 2)), bigScale, [226, 117, 250], writtenText)
smallFace = text((960 + int(textSize * smallScale), 540 - int((5 * smallScale) / 2)), smallScale, [226, 117, 250], writtenText)
border = square((0, 0), 3, [226, 117, 250], (1919, 1079), False)

lines = [bigFace, smallFace, border]

print("Shapes Placed")

thing.draw(lines)
print("")