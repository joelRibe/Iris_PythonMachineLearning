import numpy as np 

def vector_centroid(listVectors,index):
	centroid = [0] * index
	centroid = np.array(centroid)

	for listv in range(len(listVectors)):
		vector = list(map(float,listVectors[listv]))
		vector = np.array(vector)
		centroid = centroid + vector


	centroid = (centroid/index)
	return centroid


#Testing the vector_centroid function
# listVectors = []
# listVectors.append(['2','4'])
# listVectors.append(['4','8'])

# print(vector_centroid(listVectors,len(listVectors)))