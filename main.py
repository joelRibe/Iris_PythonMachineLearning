from load_data import load_data
from near_neighborhood import near_neighborhood


trainingSet,testSet = load_data('iris.txt') 
results=near_neighborhood(trainingSet,testSet)
