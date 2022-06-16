import sys
from sys import stdin
import random
import time


###############################################################################################
def countingSort(lista, max):
    size = len(lista)
    output = [0 for j in range(size)]
    count = [0 for i in range(max + 1)]

    for i in range(size-1, -1,-1):
        count[lista[i]] += 1

    for j in range(1, max + 1):
        count[j] += count[j - 1]

    for i in range(size-1,-1,-1):
        output[count[lista[i]] - 1] = lista[i]
        count[lista[i]] -= 1

    for j in range(0, size):
        lista[j] = output[j]
#######################################################################################################



def readln():
    return stdin.readline().rstrip()


def leituraB(lista,x):
    contador = 0
    while(contador < int(x)):
        for i in readln().split():
            lista.append(int(i))
        contador+=1





def binary_search(raster, end, num):
    left = 0
    right = end
    count = 0

    while (left <= right):
        mid = int((right + left) / 2)

        if (raster[mid] < num):
            count = mid + 1
            left = mid + 1
        else:
            right = mid - 1

    return count

def percentil(raster, num):
    if len(raster) == 1:
        if raster[0] < num:
            inferiores = 1
        else:
            inferiores = 0
    else:
        inferiores = binary_search(raster, len(raster)-1, num)
    return int((inferiores / len(raster)) * 100)

def leituraPercentil(lista,listaPer, conta):
    string = ""
    for i in listaPer:
        v = percentil(lista,int(i))
        conta-=1
        if conta == 0:
            string += str(v) + "\n"
        else:
            string += str(v) + " "
    return string

def AmplitudeB(lista):

    return lista[-1] - lista[0]

def MedianaB(lista):
    if(len(lista) ==  1):
        return lista[0]
    if(len(lista)%2 != 0):
        return lista[len(lista)//2+1]
    else:
        return (lista[len(lista)//2-1] + lista[len(lista)//2])//2


def mainC():
    lista = []
    final = ''

    while(True):
        listaleitura = [i for i in readln().split()]
        if(listaleitura[0] == 'RASTER'):
            leituraB(lista,listaleitura[1])
            countingSort(lista,max(lista))
            final+='RASTER GUARDADO\n'
        if(listaleitura[0] == 'PERCENTIL'):
            listanumero = [int(k) for k in readln().split()]
            final += leituraPercentil(lista,listanumero,len(listanumero))
        if(listaleitura[0] == 'AMPLITUDE'):
            final += str(AmplitudeB(lista)) + '\n'
        if(listaleitura[0] == 'MEDIANA'):
            final += str(MedianaB(lista)) + '\n'
        if(listaleitura[0] == 'TCHAU'):
            break


    print(final,end='')



################################################################################
if __name__ == "__main__":
    for i in range(100000,1000001,100000):
        lista = list(random.randint(0, 100) for k in range(i))
        lista22 = list(random.randint(0, 100) for j in range(i))
        start = time.time()
        countingSort(lista,1000)
        leituraPercentil(lista,lista22,len(lista22))
        end = time.time()
        sys.stdout=open("bruno.txt", "a+")
        print("tempo: ",i,end-start)