from load_data import load_data
from near_neighborhood import near_neighborhood
from near_centroid import calc_centroides
from near_centroid import near_centroid

trainingSet,testSet = load_data('iris.txt') 
results=near_centroid(trainingSet,testSet)

def print_results_of_near_neighborhood(results,testSet):
	hits=0
	for index in range(len(testSet)):	
		print("predicted: {0} -> actual: {1} ".format(results[index],testSet[index][4]))
		if(testSet[index][4] == results[index]):
			hits+=1

	print('')
	return (hits/len(testSet))*100

print("Accuracy: {} %" .format(print_results_of_near_neighborhood(results,testSet)))


