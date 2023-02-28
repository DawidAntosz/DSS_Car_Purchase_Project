import csv
from typing import List

import pandas as pd

class Car:
    ''' in parameters:
    ID - nazwa
    0 - Marka
    1 - Typ nadwozia
    2 - cena
    3 - moc
    4 - pojemnosc silnika
    5 - moment 
    6 - max predkosc
    7 - przyspieszenie
    8 - zuzycie paliwa
    9 - pojemnosc baku
    10 - link strony
    '''

    def __init__(self, ID:str, Marka:str, Typ:str, cena:float, moc:float, Engine_Capacity:int, Torque:int, speedMax:int, Acceleration:float ,Consumption: float,TankCapacity:int,Website: str):
        self._ID = ID
        self._Marka = Marka
        self._Type = Typ
        self._Price = cena
        self._Power = moc
        self._Engine_CC = Engine_Capacity
        self._Torque = Torque
        self._MaxSpeed = speedMax
        self._Acceleration = Acceleration
        self._Consumption = Consumption
        self._TankCapacity = TankCapacity
        self._Website = Website
        
        # self.__parametersLst = []
        self.__parametersLst = [cena,moc,Engine_Capacity,Torque,speedMax,Acceleration,Consumption,TankCapacity]

    def getParameters(self):
        print(self.__parametersLst)
        
    def __str__(self):
        return str(self._ID)+" "+ str(self._Marka)+ " "+str(self._Type)+" "+str( self._Website)

class Car2:
    def __init__(self, lst:List):
        self._Marka = lst[0]
        self._Type = lst[1]
        self._model = lst[2]
        self._parametersLst = lst[3:]
        self.modifiedParameters = []
    def getParameters(self):
        return self._parametersLst

    def __str__(self):
        return str(self._Marka)+ " "+str(self._Type) + " " + str(self._model)

    def toString(self):
        return str(self._Marka) + " " + str(self._Type) + " " + str(self._model) + str(self._parametersLst)

def getALLMatchingCarsAsLst(brand:str, type:str= ''):
    # without id, not sure if needed
    excel_data_df = pd.read_excel('DataBase.xlsx',usecols='B:L')
    rslt_df = excel_data_df[(excel_data_df['Marka'] == brand)] #& excel_data_df['Typ nadwozia'] == type]
    if type == '':
        return rslt_df.values.tolist()
    result = rslt_df[rslt_df['Typ nadwozia'] == type]
    return result.values.tolist()
def getALLMatchingCarsAsLstOfCars(brand:str, type:str= ''):
    lst = getALLMatchingCarsAsLst(brand,type)
    newLst = []
    for row in lst:
        newLst.append(Car2(row))
    return newLst

# examples
# print(getALLMatchingCarsAsLst('Opel', 'SUV'))
# getALLMatchingCars('Opel','SUV')

# print(getALLMatchingCarsAsLst('Opel'))

# print(getALLMatchingCarsAsLstOfCars('Opel', 'SUV'))