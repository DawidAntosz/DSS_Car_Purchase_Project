'''
Metoda UTA lub UTA star (do
wyboru), ewentualnie inna
wybrana metoda po uzgodnieniu
z prowadzącym

'''

from typing import List

import numpy as np
from numpy import sqrt

from dataStructures import Car2, getALLMatchingCarsAsLstOfCars



def UTA_fun(carLst:List[Car2], weights:List[int], metric = 'Euclidean'):

    print(weights) # WAGI -  [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5] TABELA PO KOLEI SZTUK
    print(metric) # STRING TYPE 

    print(carLst) # TYPU CAR2 - DATASTRUCTURES
    
    
    



    if metric == "Euclidean":
        print('metryki ')




    # ZWRACANIE - PRZYKLAD CO W GUI POTRZEBUJE ODEBRAC
    car_list = ['nazwa auta1  dane ','nazwa auta2 dane','nazwa auta3 dane ..... i tak dalej']

    return car_list