import math
import heapq
import random

def gaussCluster(center, stdDev, count=50):
    return [(random.gauss(center[0], stdDev),
             random.gauss(center[1], stdDev),
             random.gauss(center[2], stdDev)) for _ in range(count)]

def makeDummyData():
    return gaussCluster((-4,0,0), 1) + gaussCluster((4,0,0), 1)

# def euclideanDistance(x,y):
#     return math.sqrt(sum([(a-b)**2 for (a,b) in zip(x,y)]))

def euclideanDistance(x,y):
    return math.sqrt(sum([(a-b)**2 for (a,b) in zip(x,y)]))

def makeKNNClassifier(data, labels, k, distance):
    def classify(x):
        # print x
        closestPoints = heapq.nsmallest(k, enumerate(data), key=lambda y: distance(x, y[1]))
        closestLabels = [labels[i] for (i, pt) in closestPoints]
        print closestPoints

        # """
        # load distance
        closestPoints = [(node_id, distance(x, vector)) for node_id, vector in closestPoints]
        print closestPoints

        # normalize, and weighed (1-)
        sum_values = sum([_[1] for _ in closestPoints])
        closestPoints = [(node_id, 1-float(dis)/sum_values) for node_id, dis in closestPoints]
        print closestPoints
        # """
        return max(set(closestLabels), key=closestLabels.count)

    return classify

if __name__ == "__main__":
   import sys

   k = sys.argv[1] if len(sys.argv) == 2 else 8

   trainingPoints = makeDummyData() # has 50 points from each class
   trainingLabels = [1] * 50 + [2] * 50  # an arbitrary choice of labeling

   f = makeKNNClassifier(trainingPoints, trainingLabels, k, euclideanDistance)
   print f((1,1,0))
   # print f((-3,0))
   # print f((3,0))
   # print f((0,0))

   # print trainingPoints
