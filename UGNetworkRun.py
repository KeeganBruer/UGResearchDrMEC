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

def createAndTrainNetwork():
    dataPrefix = input(str(dataPrefixs) + "\nEnter Data Prefix: ")
    UGNetwork.trainNetwork(dataPrefix)

def evaluateNetwork():
    dataPrefix = input(str(dataPrefixs) + "\nEnter Data Prefix: ")
    UGNetwork.evaluate(dataPrefix)

def ExtractWeightsToFile():
    dataPrefix = input(str(dataPrefixs) + "\nEnter Data Prefix: ")
    NWD.extractWeightsToFile(dataPrefix)

def addLabelsToWeightFile():
    dataPrefix = input(str(dataPrefixs) + "\nEnter Data Prefix: ")
    AL2W.addLabelsToWeightFile(dataPrefix)


def EvaluateAndSortWeights():
    dataPrefix = input(str(dataPrefixs) + "\nEnter Data Prefix: ")
    weightsort.EvaluateAndSortWeights(dataPrefix)

def ExtractImportantWeights():
    EIW.ExtractImportantWeights(dataPrefixs)

def allTheAbove():
    dataPrefix = input(str(dataPrefixs) + "\nEnter Data Prefix: ")
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
    userInput = int(input(">>>"))
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
    switcher.get(userInput, "Invalid Input")()