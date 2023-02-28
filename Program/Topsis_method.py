'''
Zaimplementowanie metody Topsis z utworzeniem rankingu oraz
wyborem rozwiązania kompromisowego dla przypadku dyskretnego
'''
from typing import List

import numpy as np
from numpy import sqrt

from dataStructures import Car2, getALLMatchingCarsAsLstOfCars

def Topsis(carLst:List[Car2], weights:List[int], metric = 'Euclidean'):
    # make sure working parameters are set to empty lst
    for car in carLst:
        car.modifiedParameters = []
    scalingFactor = np.array([0 for _ in carLst[0].getParameters()])


    # scaling factor
    for car in carLst:
        for i,criteria in enumerate(car.getParameters()):
            scalingFactor[i] += criteria ** 2
    scalingFactor = np.sqrt(scalingFactor)
    # print(scalingFactor)

    for car in carLst:
        for i,criteria in enumerate(car.getParameters()):
            if i == 0 or i== 6: # easy ideal and worst point calculation invert price and consumption
                car.modifiedParameters.append(-criteria * weights[i] /scalingFactor[i])
            else:

                car.modifiedParameters.append(criteria * weights[i] /scalingFactor[i])

    notIdPoint = np.inf * np.ones(len(carLst[0].modifiedParameters), float)
    IdPoint = -np.inf * np.ones(len(carLst[0].modifiedParameters), float)

    # getting best and worst parameters of all vehicles
    for car in carLst:
        for i,parameter in enumerate(car.modifiedParameters):
            IdPoint[i] = max(IdPoint[i],parameter)
            notIdPoint[i] = min(notIdPoint[i],parameter)

    # print(IdPoint)
    # print(notIdPoint)
    c = []
    for i,car in enumerate(carLst):
        dBest = 0
        dWorst = 0
        # euclides metric
        if metric == 'Euclidean':
            for j,parameter in enumerate(car.modifiedParameters):
                dBest += np.abs(parameter - IdPoint[j])**2
                dWorst += np.abs(parameter - notIdPoint[j])**2
            dBest = sqrt(dBest)
            dWorst = sqrt(dWorst)
        if metric == 'Chebyshev':
            for j, parameter in enumerate(car.modifiedParameters):
                dBest = max(IdPoint[j] - parameter,dBest)
                dWorst = max(parameter - notIdPoint[j],dWorst)

        c.append((dBest/(dWorst + dBest),i)) # for the best point

    print(c)
    sortedLst = c.copy()
    sortedLst.sort(key=lambda x: x[0])
    sortedLst.reverse()
    # print(sortedLst)


    toReturn = [carLst[i].toString() for _,i in sortedLst]
    print(toReturn)
    return toReturn

#Topsis(getALLMatchingCarsAsLstOfCars('BMW', 'SUV'), [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],metric='Chebyshev')