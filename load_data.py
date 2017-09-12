import numpy as np

def load_data(fileName):

	dataset = np.genfromtxt(fileName,delimiter=' ', dtype='str')

	setosas = np.where( dataset == 'Setosa')[0].tolist()
	versicolors = np.where( dataset == 'Versicolor')[0].tolist()
	virginicas = np.where( dataset == 'Virginica')[0].tolist()


	np.random.shuffle(setosas)
	np.random.shuffle(versicolors)
	np.random.shuffle(virginicas)



	trainingSet = []
	testSet = []

	for sets in [setosas,versicolors,virginicas]:
		for index in range(0,50):
			if index <= 39:
				trainingSet.append(dataset[sets[index]].tolist())
			else:
				testSet.append(dataset[sets[index]].tolist())
	return [trainingSet,testSet]



# [load1,load2] = load_data('iris.txt')
# print(load1[40:80])



