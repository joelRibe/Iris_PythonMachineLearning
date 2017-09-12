import numpy as np
from distEuclidian import dist_euclidiana_np
from vectorCentroid import vector_centroid
from load_data import load_data # for Test

def centroides(trainingSetSetosas,trainingSetVersicolors,trainingSetVirginicas):
	
	setosaCentroid = vector_centroid(trainingSetSetosas)

	versicolorCentroid = vector_centroid(trainingSetVersicolors)

	virginicaCentroid = vector_centroid(trainingSetVirginicas)

	return [setosaCentroid,versicolorCentroid,virginicaCentroid]





# def near_centroid()