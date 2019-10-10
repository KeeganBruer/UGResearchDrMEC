def getNetworkData(fileName, split):
    largest = 0;
    train_data = []
    train_labels = []
    file = open(fileName)
    lines = file.readlines()
    for line in lines:
        line = line.replace("\n", "")
        if (line != ""):
            data = []
            lineArray = line.split(split)
            labels = []
            for i in range(5):
                value = lineArray[i].strip().replace("\n", "")
                labels.append(float(value))
            train_labels.append(labels)
            for i in range(5, len(lineArray)):
                value = lineArray[i].strip().replace("\n", "")
                if (value != ""):
                    if (float(value) > largest):
                        largest = float(value)
                    data.append(float(value))
            train_data.append(data)
    return train_data, train_labels, largest

def getNetworkAccuracy(results, train_labels, count=0):
    acc = 0;
    for i in range(len(results)):
        output = results[i]
        choice = 0
        largest = 0
        for val in range(len(output)):
            if (output[val] > largest):
                largest = output[val]
                choice = val + 1
        labels = train_labels[i]
        labelChoice = 0
        for val in range(len(labels)):
            if(labels[val] == 1):
                labelChoice = val+1
        if (labelChoice == choice):
            acc += 1
        if (i < count):
            print(train_labels[i])
            print(str(labelChoice) + " " + str(choice))
    return (acc / len(results))

def getResultCount(results):
    outputCount = [0, 0, 0, 0, 0]
    for i in range(len(results)):
        choice = 0
        largest = 0
        for j in range(len(results[i])):
            if (results[i][j] > largest):
                largest = results[i][j]
                choice = j
        outputCount[choice] += 1
    return outputCount
def extractWeightsToFile(fileBase, model):
    model = load_model('Data/Models/MEC.h5')
    weights = model.layers[1].get_weights()[0]
    biases  = model.layers[1].get_weights()[1]
    weightFile = open("data/Weights/" + fileBase + "_weights.txt", "w")
    contentWeight = ""
    for feature in weights:
        for node in feature:
            if (node > 0):
                contentWeight += " {0:2.4f}".format(node) + " "
            else:
                contentWeight += "-{0:4.4f}".format(abs(node)) + " "
        contentWeight += "\n"
    weightFile.write(contentWeight)
    weightFile.close()
