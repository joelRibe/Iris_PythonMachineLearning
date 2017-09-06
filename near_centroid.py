import numpy as np
from distEuclidian import dist_euclidiana_np
from vectorCentroid import vector_centroid
from load_data import load_data # for Test

def centroides(trainingSet):
	
	# setosaCentroid = vector_centroid(np.where( trainingSet == 'Setosa')[:4] , len(trainingSet[0]))

	# versicolorCentroid = vector_centroid(np.where( trainingSet == 'Versicolor')[:4], len(trainingSet[0]))

	# virginicaCentroid = vector_centroid(np.where( trainingSet == 'Virginica')[:4], len(trainingSet[0]))

	return [setosaCentroid,versicolorCentroid,virginicaCentroid]


#testing the 'centroides' function
# trainingSet,testSet = load_data('iris.txt') 
# centroides = centroides(trainingSet)

# print(centroides[0])
# print(centroides[1])
# print(centroides[2])
