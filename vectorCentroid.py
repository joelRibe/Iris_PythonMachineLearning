import numpy as np 

def vector_centroid(listVectors):
	centroid = [0] * len(listVectors[0])
	centroid = np.array(centroid)

	for listv in range(len(listVectors)):
		vector = list(map(float,listVectors[listv]))
		vector = np.array(vector)
		centroid = centroid + vector


	centroid = (centroid/len(listVectors))
	return centroid


#Testing the vector_centroid function
# listVectors = []
# listVectors.append(['2','4'])
# listVectors.append(['4','8'])
# listVectors.append(['2','8'])

# print(vector_centroid(listVectors))