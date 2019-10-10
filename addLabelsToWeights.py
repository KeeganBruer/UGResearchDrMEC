def addLabelsToWeightFile(dataPrefix):
    file = open("data/weights/" + dataPrefix + "_weights.txt")
    labels = open("data/weights/Labels.txt").readlines()
    fileOut = open("data/WeightsAndLabels/" + dataPrefix + "_weights.txt", "w+")

    lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].replace("\n", "") + " " + labels[i]
    fileOut.writelines(lines)
    fileOut.close()