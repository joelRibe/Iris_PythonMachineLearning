from load_data import load_data
from near_neighborhood import near_neighborhood


trainingSet,testSet = load_data('iris.txt') 
results=near_neighborhood(trainingSet,testSet)

def print_results(results,testSet):
	hits=0
	for index in range(len(testSet)):	
		print("predicted: {0} -> actual: {1} ".format(results[index],testSet[index][4]))
		if(testSet[index][4] == results[index]):
			hits+=1

	print('')
	return (hits/len(testSet))*100

print("Accuracy: {} %" .format(print_results(results,testSet)))


