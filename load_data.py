import numpy as np

dataset = np.genfromtxt('iris.txt',delimiter=' ', dtype='str')

setosas = np.where( dataset == 'Setosa')[0].tolist()
versicolors = np.where( dataset == 'Versicolor')[0].tolist()
virginicas = np.where( dataset == 'Virginica')[0].tolist()


np.random.shuffle(setosas)
np.random.shuffle(versicolors)
np.random.shuffle(virginicas)



trainingSet = []
testSet = []

for index in range(0,50):
    if index <= 39:
        trainingSet.append(dataset[setosas[index]].tolist())
        trainingSet.append(dataset[versicolors[index]].tolist())
        trainingSet.append(dataset[virginicas[index]].tolist())
    else:
        testSet.append(dataset[setosas[index]].tolist())
        testSet.append(dataset[versicolors[index]].tolist())
        testSet.append(dataset[virginicas[index]].tolist())
