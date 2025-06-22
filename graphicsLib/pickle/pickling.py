import pickle
out = {}

with open("letters.txt", "r") as activeFile:
    text = activeFile.read()


# take the strings of points and convert them into integers and put them into tuples
letterText = text.split("\n")
letterTuples = []
for letterset in letterText[0:42]:
    temp = letterset.split(", ")
    letterList = [temp[0]]
    for point in temp[1:]:
        extractedpoint = point[1:len(point) - 1].split(",")
        extractedpointint = []
        for i in extractedpoint:
            extractedpointint.append(int(i))
        
        letterList.append(tuple(extractedpointint))
    letterTuples.appevnd(letterList)

# change the values in the list 
temp = []
for letterset in letterTuples:
    newLetterset = []
    for point in letterset[2:]:
        listedpoint = list(point)
        listedpoint[0] += 1
        listedpoint[1] += 2
        newLetterset.append(tuple(listedpoint))
    temp.append(letterset[0:2] + newLetterset)
letterTuples = temp

# Visualize characters to ensure they're valid
for letterset in letterTuples:
    xlen = letterset[1][0]
    ylen = 5
    matrix = [[" " for i in range(xlen)] for i in range(ylen)]

    for point in letterset[2:]:
        matrix[4 - point[1]][point[0]] = "X"
    
    for i in matrix:
        print(i)
    print()

# format into a dictionary for ease of access
for letterset in letterTuples:
    out.update({letterset[0]:[letterset[1],letterset[2:]]})
    
out.update({" ": [(3,5),()]})

# Pickle the dictionary
with open("letters.pkl", "wb") as pickleFile:
    pickle.dump(out, pickleFile)