from load_data import *
from near_neighborhood import *
from near_centroid import *

trainingSet, testSet = load_data('iris.txt')
results1 = near_neighborhood(trainingSet, testSet)
results2 = near_centroid(trainingSet, testSet)


def print_results_of_near_neighborhood(results, testSet):
    hits = 0
    for index in range(len(testSet)):
        print(
            "predicted: {0} -> actual: {1} ".format(results[index], testSet[index][4]))
        if(testSet[index][4] == results[index]):
            hits += 1

    print('')
    return (hits / len(testSet)) * 100


print("Accuracy: {} %" .format(
    print_results_of_near_neighborhood(results1, testSet)))

print("Accuracy: {} %" .format(
    print_results_of_near_neighborhood(results2, testSet)))
