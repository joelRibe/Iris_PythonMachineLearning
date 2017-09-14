import numpy as np
from distEuclidian import dist_euclidiana_np
from vectorCentroid import vector_centroid
from load_data import load_data  # for Test


def calc_centroides(trainingSet):
    trainingSet = np.array(trainingSet)
    trainingSet = trainingSet[:, :4].tolist()

    setosaCentroid = [vector_centroid(trainingSet[:40]), 'Setosa']

    versicolorCentroid = [vector_centroid(trainingSet[40:80]), 'Versicolor']

    virginicaCentroid = [vector_centroid(trainingSet[80:120]), 'Virginica']

    return [setosaCentroid, versicolorCentroid, virginicaCentroid]


def near_centroid(trainingSet, testSet):
    resultsList = []

    centroides = calc_centroides(trainingSet)

    for test in testSet:
        dist = dist_euclidiana_np(test, centroides[0][0], 4)
        label = 'Setosa'
        for centros in centroides:
            dist1 = dist_euclidiana_np(test, centros[0], 4)
            if(dist > dist1):
                label = centros[1]
                dist = dist1

        resultsList.append(label)

    return resultsList
