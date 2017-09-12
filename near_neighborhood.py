from distEuclidian import dist_euclidiana_np

def near_neighborhood(trainingSet , testSet):
	resultsList = []

	for test in testSet:
		dist = dist_euclidiana_np(test,trainingSet[0],len(trainingSet[0])-1)
		label='Setosa'
		for training in trainingSet:
			if(dist>dist_euclidiana_np(test,training,len(training)-1)):
				dist=dist_euclidiana_np(test,training,len(training)-1)
				label=training[len(training)-1]

		resultsList.append(label)

	return resultsList
