def NormalizeData(dataPrefix):
    inFile = open("Data/FaceEvaluations/" + dataPrefix + ".txt")
    lines = inFile.readlines()
    largest = -10
    smallest = 10
    for i in range(len(lines)):
        line = " ".join(lines[i].split("  ")).split(" ")
        for item in line:
            if (item.strip() != ""):
                if (float(item) > largest): 
                    largest = float(item.strip())
                elif (float(item) < smallest):
                    smallest = float(item.strip())
    outLines = []
    for i in range(len(lines)):
        line = " ".join(lines[i].split("  ")).split(" ")
        newLine = []
        for item in line:
            if (item.strip() != ""):
                newLine.append("{0:.2f}".format(map(float(item.strip()), smallest, largest,0, 1)))
        outLines.append(" ".join(newLine) + "\n")
    outFile = open("Data/NormalizedEvaluations/"+ dataPrefix + ".txt", "w+")
    outFile.writelines(outLines)

def map(X, A, B, C, D):
    return (X-A)/(B-A) * (D-C) + C
NormalizeData("KSB")