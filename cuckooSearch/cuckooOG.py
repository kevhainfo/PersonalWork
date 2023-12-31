from problem import inputMatrix
from random import uniform
from random import randint
from tsp_LK import *
import math

distanceMatrix = inputMatrix


def levyFlight(u):
    return math.pow(u, -1.0 / 2.0)


def randF():
    return uniform(0.0001, 0.9999)


def calculateDistance(path):
    index = path[0]
    distance = 0
    for nextIndex in path[1:]:
        distance += distanceMatrix[index][nextIndex]
        index = nextIndex
    return distance + distanceMatrix[path[-1]][path[0]];


def swap(sequence, i, j):
    temp = sequence[i]
    sequence[i] = sequence[j]
    sequence[j] = temp


def swapMove(nest, a, c):
    nest = nest[0][:]
    swap(nest, a, c)
    return (nest, calculateDistance(nest))


def doubleSwapMove(nest, a, b, c, d):
    nest = nest[0][:]
    swap(nest, a, b)
    swap(nest, b, d)
    return (nest, calculateDistance(nest))


numNests = 15

maxGen = 25

n = len(inputMatrix)

nests = []

initPath = list(range(0, n))

index = 0
for i in range(numNests):
    if index == n - 1:
        index = 0
    swap(initPath, index, index + 1)
    index += 1
    nests.append((initPath[:], calculateDistance(initPath)))

nests.sort(key=lambda tup: tup[1])
seed = randint(0, numNests - 1)
LK_nest = tsp_LK(distanceMatrix, nests[seed][0], nests[seed][1])
print(LK_nest)
lowestValue = 10000000
lowestNest = nests[0]
for t in range(maxGen):
    cuckooNest = nests[randint(0, numNests - 1)]
    if (levyFlight(randF()) > 2):
        cuckooNest = doubleSwapMove(cuckooNest, randint(0, n - 1), randint(0, n - 1), randint(0, n - 1),
                                    randint(0, n - 1))
    else:
        cuckooNest = swapMove(cuckooNest, randint(0, n - 1), randint(0, n - 1))

    randomNestIndex = randint(0, numNests - 1)
    if (nests[randomNestIndex][1] > cuckooNest[1]):
        nests[randomNestIndex] = cuckooNest
    for i in range(0, numNests):
        nests[i] = doubleSwapMove(nests[i], randint(0, n - 1), randint(0, n - 1), randint(0, n - 1),
                                  randint(0, n - 1))
        nests[i] = tsp_LK(distanceMatrix, nests[i][0], nests[i][1])
    nests.sort(key=lambda tup: tup[1])
    if lowestValue > nests[0][1]:
        lowestNest = nests[0]
        lowestValue = nests[0][1]
    print(lowestNest)
print
"CUCKOO's SOLUTION"
nests.sort(key=lambda tup: tup[1])
print(nests[0])