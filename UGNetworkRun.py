import UGNetwork
import NetworkDataUtils as NWD
import weightsort
import addLabelsToWeights as AL2W
import ExtractImportantWeights as EIW

#Data Conditions
dataPrefixs = ["ADG", "KMS", "KSB", "Mds", "MEC", "RCK"]
running = True

def exitProgram():
    running = False

def createAndTrainNetwork(dataPrefix):
    UGNetwork.trainNetwork(dataPrefix)

def evaluateNetwork(dataPrefix):
    UGNetwork.evaluate(dataPrefix)

def ExtractWeightsToFile(dataPrefix):
    NWD.extractWeightsToFile(dataPrefix)

def addLabelsToWeightFile(dataPrefix):
    AL2W.addLabelsToWeightFile(dataPrefix)


def EvaluateAndSortWeights(dataPrefix):
    weightsort.EvaluateAndSortWeights(dataPrefix)

def ExtractImportantWeights(dataPrefix):
    EIW.ExtractImportantWeights(dataPrefixs)

def allTheAbove(dataPrefix):
    UGNetwork.trainNetwork(dataPrefix)
    UGNetwork.evaluate(dataPrefix)
    NWD.extractWeightsToFile(dataPrefix)
    AL2W.addLabelsToWeightFile(dataPrefix)
    weightsort.EvaluateAndSortWeights(dataPrefix)

while(running):
    print("==MENU==")
    print("1: Create and Train Network")
    print("2: Evaluate Network")
    print("3: Extract Weights To File")
    print(" : Normalize Network Weights")
    print("4: Add Labels To Weight Files")
    print("5: Evaluate and Sort Weights")
    print("6: Extract Ranked Weights")
    print("7: All The Above")
    switcher = {
        0: exitProgram,
        1: createAndTrainNetwork,
        2: evaluateNetwork,
        3: ExtractWeightsToFile,
        4: addLabelsToWeightFile,
        5: EvaluateAndSortWeights,
        6: ExtractImportantWeights,
        7: allTheAbove
    }
    userInput = int(input(">>>"))
    dataPrefix = input(str(dataPrefixs) + "\nEnter Data Prefix: ")
    if dataPrefix == "All":
        for dataPrefix1 in dataPrefixs:
            print(dataPrefix1)
            switcher.get(userInput, "Invalid Input")(dataPrefix1)
    else:
        switcher.get(userInput, "Invalid Input")(dataPrefix)
	





