import weightsort

def ExtractImportantWeights(dataPrefixs):
    file = open("Data/sorted/" + dataPrefixs[0] + "_weights.txt")
    outfile = open("data/ImportantWeights/ranked.txt", "w+")
    lines = file.readlines()
    outLines = []
    for i in range(len(lines)):
        lineArray = lines[i].split("  ")
        newLine = lineArray.pop().strip()
        newArray = [newLine]
        for count in range(len(dataPrefixs)):
            newArray.append(150)  
        outLines.append(newArray)
    for count in range(len(dataPrefixs)):
        prefix = dataPrefixs[count]
        lines = open("Data/sorted/" + prefix + "_weights.txt").readlines()
        for i in range(len(lines)):
            line = lines[i].split("  ").pop().strip()
            for j in range(len(outLines)):
                if (line == outLines[j][0]):
                    if (outLines[j][count+1] > i+1):
                        outLines[j][count+1] = i+1
    for i in range(len(outLines)):
        largest = 0;
        for j in range(1, len(outLines[i])):
            if (int(outLines[i][j]) > largest):
                largest = int(outLines[i][j])
        outLines[i].append(largest)
    weightsort.quickSort(outLines, len(outLines[0])-1, 0, len(outLines)-1)
    outputArray = []
    for i in range(len(outLines)):
        outLine = ""
        for j in range(len(outLines[i])):
            outLine += str(outLines[i][j])
            if (j < len(outLines[i])-1):
                outLine += " | "
        outputArray.append(outLine + "\n") 
    outfile.writelines(outputArray)
    outfile.close()
        
ExtractImportantWeights(["KMS", "KSB"])