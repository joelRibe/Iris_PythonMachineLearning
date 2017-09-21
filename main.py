from load_data import *
from near_neighborhood import *
from near_centroid import *
from normalization_data import *

# whitout normalization data
# trainingSet, testSet = load_data('iris.txt')
# results1 = near_neighborhood(trainingSet, testSet)
# results2 = near_centroid(trainingSet, testSet)

# with normalization data
trainingSet, testSet = load_data('iris.txt')
trainingSet_norm, testSet_norm = data_normalization(trainingSet, testSet)
results1 = near_neighborhood(trainingSet_norm, testSet_norm)
results2 = near_centroid(trainingSet_norm, testSet_norm)


def print_results_of_near_neighborhood_or_centroid(results, testSet, algorithm):
    print('Type of Algorithm : {}' .format(algorithm))
    hits = 0
    for index in range(len(testSet)):
        print(
            "predicted: {0} -> actual: {1} ".format(results[index], testSet[index][4]))
        if(testSet[index][4] == results[index]):
            hits += 1

    print('')
    return (hits / len(testSet)) * 100


print("Accuracy: {} %" .format(
    print_results_of_near_neighborhood_or_centroid(results1, testSet, 'Near-Neighborhood')))

print('')

print("Accuracy: {} %" .format(
    print_results_of_near_neighborhood_or_centroid(results2, testSet, 'Near-Centroid')))
