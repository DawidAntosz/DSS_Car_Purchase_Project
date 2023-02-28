import dataStructures as sd

'''
Implementacja metody zbiorów
odniesienia (RSM) w problemach
wyboru rozwiązania
kompromisowego oraz z
utworzeniem rankingu
'''
import numpy as np


'''Oblicza pole obejmowane przez prostokąt o krawędziach z dwóch punktów'''
def count_area( a1, a2):
    area=1
    for i in range(len(a1)):
        area=area*(a1[i]-a2[i])
    return area
  

'''Pomocnicza do testów - zamienić na używaną do obliczenia naszej normy
- liczy odległość między dwoma punktami według normy euklidesa'''

def count_norm(a1,a2):
    sum=0
    for i in range(len(a1)):
        sum+=(a1[i]-a2[i])**2
    return np.sqrt(sum)

'''Liczy funkcję skoringową'''
def count_f(u,a_plus,a_minus):
    d_minus=count_norm(u,a_minus)
    #print(u,d_minus,'dminus')
    d_plus=count_norm(u,a_plus)
    #print(u,d_plus,'dplus')
    return d_minus/(d_minus+d_plus)

'''Liczy wartość dla punktu po której będziemy porównywać ten punkt z innymi '''
def count_big_f(tab_a_plus,tab_a_minus,u):
    w_sum=0
    big_f=0
    for i in range(len(tab_a_plus)):
        for j in range(len(tab_a_minus)):
            w=count_area(tab_a_plus[i],tab_a_minus[j])
            print(w,'area')
            big_f+=w*count_f(tab_a_plus[i],tab_a_minus[j],u)
            w_sum+=w
    return big_f/w_sum


def normalize( list, weight ):

    il_param=len(list[0]._parametersLst)
    '''Stworzenie listy w modifiedParameters i pierwiastka z sumy kwadratów wartości'''
    sum=np.zeros(il_param)
    for i in list:
        i.modifiedParameters=np.zeros(il_param+1)
        for j in range(il_param):
            sum[j]+=i._parametersLst[j]**2
    sum=np.sqrt(sum)
    
    '''Właściwa normalizacja z wpisaniem wartości do modifiedParameters '''
    for i in list:
        for j in range(len(i._parametersLst)):
            if j!=0 and j!=6:
                i.modifiedParameters[j]=i._parametersLst[j]/sum[j]*weight[j]
            else:
                i.modifiedParameters[j]=(1-i._parametersLst[j]/sum[j])*weight[j]

def sortuj(list):
    n=len(list)
    flag=1
    while n>1 and flag==1:
        flag=0
        for l in range(0,n-1):
            if list[l][-1]>list[l+1][-1]:
                list[l],list[l+1]=list[l+1],list[l]
                flag=1        
        n=n-1
    return list


def RMS_fun(Data_search: list, weight, metric):
    weight.pop(0)
    weight.pop(0)

    normalize(Data_search,weight)

    a_plus=[[0.025, 0.0037, 0.007, 0.0046, 0.0132, 0.0155,0.057, 0.017],
    [0.027, 0.0021, 0.008, 0.0051, 0.0145, 0.0150,0.054, 0.018],
    [0.026, 0.0026, 0.007, 0.0049, 0.0153, 0.0143,0.053, 0.011],
    [0.028, 0.0027, 0.006, 0.0053, 0.0147, 0.0159,0.058, 0.016],]

    a_minus=[[0.3,0.34,0.26,0.27,0.31,0.22,0.33,0.35],
    [0.28,0.25,0.19,0.3,0.25,0.3,0.24,0.26],
    [0.23,0.25,0.27,0.28,0.24,0.26,0.29,0.33],
    [0.27,0.24,0.28,0.29,0.21,0.25,0.31,0.22]]

    for i in range(len(weight)):
        for j in range(len(a_plus)):
            a_plus[j][i]*=weight[i]
            a_minus[j][i]*=weight[i]


    gui_tab=[]
    for i in range(len(Data_search)):
        score_value=count_big_f(a_plus,a_minus,Data_search[i].modifiedParameters)
        score_value=np.round(score_value,4)
        data=[Data_search[i]._Marka,Data_search[i]._Type,Data_search[i]._model,Data_search[i]._parametersLst,score_value]
        gui_tab.append(data)
        

    gui_tab=sortuj(gui_tab)
    tab_return = []

    for car in gui_tab:
        str_data = ''

        for data in car:
            str_data += str(data) + " "
        tab_return.append(str_data)

    print(tab_return)
    return tab_return