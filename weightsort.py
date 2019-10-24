def partition(arr,pos,low,high): 
    i = ( low-1 )         # index of smaller element 
    pivot = arr[high][pos]     # pivot 
  
    for j in range(low , high): 
  
        # If current element is smaller than or 
        # equal to pivot 
        if   arr[j][pos] <= pivot: 
          
            # increment index of smaller element 
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
  
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i+1 ) 
  
# The main function that implements QuickSort 
# arr[] --> Array to be sorted, 
# low  --> Starting index, 
# high  --> Ending index 
  
# Function to do Quick sort 
def quickSort(arr,pos,low,high): 
    if low < high: 
  
        # pi is partitioning index, arr[p] is now 
        # at right place 
        pi = partition(arr,pos,low,high) 
  
        # Separately sort elements before 
        # partition and after partition 
        quickSort(arr,pos, low, pi-1) 
        quickSort(arr,pos, pi+1, high) 

def EvaluateAndSortWeights(dataPrefix):
    file = open("data/WeightsAndLabels/" + dataPrefix + "_weights.txt")
    outFile = open("data/sorted/" + dataPrefix + "_weights.txt", "w+")
    lines = file.readlines()

    for i in range(len(lines)):
        ranking = 0;
        data = lines[i].strip().split("  ")
        data = " ".join(data).split(" ")
        ranking += float(data[0]) * 2
        ranking += float(data[1]) * 1
        ranking += float(data[2]) * 0
        ranking += float(data[3]) * 1
        ranking += float(data[4]) * 2
        lines[i] = "{0:.2f}".format(float(ranking)) + " " + lines[i].replace("\n", "") + "\n"
        lines[i] = lines[i].split(" ")
    print(lines)
    quickSort(lines,0, 0, len(lines)-1)
    for i in range(len(lines)):
        lines[i] = " ".join(lines[i])
    lines2 = []
    for i in range(len(lines)):
        lines2.insert(0, lines[i])
    outFile.writelines(lines2)
    outFile.close()
	
