# Method : Constant Norm
# this simple method of normalization consists in maiintaining constants and equals "one" the norm of vectors
# that a dataset .
import math
import numpy as np


def data_normalization(trainingSet, testSet):
    trainingSet_normalized = []

    for training_norm in trainingSet:
        norm = math.sqrt((float(training_norm[0]) * 2) + (float(training_norm[1]) * 2) +
                         (float(training_norm[2]) * 2) + (float(training_norm[3]) * 2))

        trainingSet_normalized.append([float(training_norm[0]) / norm, float(training_norm[1]) / norm,
                                       float(training_norm[2]) / norm, float(training_norm[3]) / norm, training_norm[4]])

    testSet_normalized = []

    for test_norm in testSet:
        norm = math.sqrt((float(test_norm[0]) * 2) + (float(test_norm[1]) * 2) +
                         (float(test_norm[2]) * 2) + (float(test_norm[3]) * 2))

        testSet_normalized.append([float(test_norm[0]) / norm, float(test_norm[1]) / norm,
                                   float(test_norm[2]) / norm, float(test_norm[3]) / norm, test_norm[4]])

    return [trainingSet_normalized, testSet_normalized]

# trainingSet = [['1', '2', '3', '4', 'Setosa'],
#                ['5', '3', '1', '1', 'Virginica']]

# testSet = [['1', '2', '4', '7', 'Versicolor']]


# print(data_normalization(trainingSet, testSet))
