#import copy


def amplitude1(raster):
    max = 0
    min = 100000
    for i in raster:
        if i >= max:
            max = i
        if i <= min:
            min = i
    return max - min


def mediana1(raster):
    size = len(raster)
    soma = 0
    if size == 1:
        return raster[0]
    for i in range(size):
        count = 0
        numberof = 0
        for j in range(size):
            if raster[i] > raster[j]:
                count += 1
            if raster[i] == raster[j]:
                numberof += 1

        if count < (size / 2) and count + numberof >= size / 2 and soma == 0:
            if size % 2 != 0:
                return raster[i]
            soma += raster[i]
        if count < (size / 2) + 1 and count + numberof >= size / 2 + 1 and soma > 0:
            return (raster[i] + soma) // 2


def percentil1(raster, num):
    size = 0
    inferiores = 0
    for i in raster:
        if i < num:
            inferiores += 1
        size += 1
    return int((inferiores / size) * 100)


# ----------------------------------------------------------------------------------------------------------------------
#sorted_r = insertionSort(raster)

def insertionSort(raster):
    #aux = copy.deepcopy(raster)
    for i in range(1, len(raster)):
        key = raster[i]
        j = i - 1
        while j >= 0 and key <raster[j]:
            raster[j + 1] = raster[j]
            j -= 1
        raster[j + 1] = key
    return raster


import math

def mediana_elementar(raster):
    if len(raster) == 1:
        return raster[0]
    size = len(raster)
    if size % 2 == 0:
        return (raster[int(size / 2) - 1] + raster[int(size / 2)]) // 2
    else:
        return raster[math.ceil(size / 2)]


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



def percentil_elementar(raster, num):
    if len(raster)==1:
        if raster[0] < num:
            inferiores=1
        else:
            inferiores=0
    else:
        inferiores = binary_search(raster, len(raster)-1, num)
    return int((inferiores / len(raster)) * 100)


def amplitude_elementar(raster):
    if len(raster) == 1:
        return 0
    return raster[len(raster) - 1] - raster[0]


# ----------------------------------------------------------------------------------------------------------------------
#sorted_r = quickSort(copy.deepcopy(raster), 0, len(raster)-1)
def insertion(raster,low,high):
    for i in range(low + 1, high):
        key = raster[i]
        j = i-1
        while j >= 0 and key < raster[j] :
            raster[j+1] = raster[j]
            j-=1

        raster[j+1] = key




def partitionF(array, start, end):
    low = start + 1
    high = end
    middle = int((high+low)/2)
    if (array[start]) > array[middle]:
        array[middle], array[start] = array[start], array[middle]
    if (array[start]) > array[middle]:
        array[end], array[start] = array[start], array[end]
    if (array[middle]) > array[high]:
        array[end], array[middle] = array[middle], array[end]

    pivot = array[high]

    while True:

        while low <= high and array[high] >= pivot:
            high = high - 1


        while low <= high and array[low] <= pivot:
            low = low + 1


        if low <= high:
            array[low], array[high] = array[high], array[low]

        else:

            break

    array[start], array[high] = array[high], array[start]

    return high

def quickSort(array, start, end):
    cutoff = 30
    if len(array) == 1:
        return array
    if start + cutoff > end:
        insertion(array, start, end + 1)
    else:
        p = partitionF(array, start, end)
        quickSort(array, start, p-1)
        quickSort(array, p+1, end)


def percentil(raster, num):
    if len(raster) == 1:
        if raster[0] < num:
            inferiores = 1
        else:
            inferiores = 0
    else:
        inferiores = binary_search(raster, len(raster)-1, num)
    return int((inferiores / len(raster)) * 100)


def amplitude(raster):
    if len(raster) == 1:
        return 0
    quickSort(raster, 0, len(raster) - 1)
    return raster[len(raster) - 1] - raster[0]


def mediana(raster):
    if len(raster) == 1:
        return raster[0]
    size = len(raster)
    if size % 2 == 0:
        return (raster[int(size / 2) - 1] + raster[int(size / 2)]) // 2
    else:
        return raster[math.ceil(size / 2)]



#----------------------------------------------------------------------------------------------------------------------

def countingSort(lista):
    max_element = int(max(lista))
    min_element = int(min(lista))
    range_of_elements = max_element - min_element + 1
    count_arr = [0 for _ in range(range_of_elements)]
    output_arr = [0 for _ in range(len(lista))]

    for i in range(0, len(lista)):
        count_arr[lista[i] - min_element] += 1

    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i - 1]

    for i in range(len(lista) - 1, -1, -1):
        output_arr[count_arr[lista[i] - min_element] - 1] = lista[i]
        count_arr[lista[i] - min_element] -= 1


    for i in range(0, len(lista)):
        lista[i] = output_arr[i]

    return lista


#----------------------------------------------------------------------------------------------------------------------
import sys
import time

def func(name):
    sys.stdin = open(name, "r")
    line = input().split()
    global linha, coluna
    raster = list()
    while line[0] != "TCHAU":
        sys.stdout = open("out.txt", "w")
        if line[0] == "RASTER":
            linha = int(line[1])
            coluna = int(line[2])
            for i in range(linha):
                line = input().split()
                for j in range(coluna):
                    raster.append(int(line[j]))
            print("RASTER GUARDADO")
        elif line[0] == "AMPLITUDE":
            #raster = insertionSort(raster)
            #quickSort(copy.deepcopy(raster), 0, len(raster) - 1)
            countingSort(raster)
            print(amplitude(raster))
        elif line[0] == "MEDIANA":
            #raster = insertionSort(raster)
            #quickSort(copy.deepcopy(raster), 0, len(raster)-1)
            countingSort(raster)
            print(mediana(raster))
        elif line[0] == "PERCENTIL":
            start = time.time()
            #raster = insertionSort(raster)
            #quickSort(raster, 0, len(raster) - 1)
            countingSort(raster)
            aux = input().split()
            print(' '.join(str(percentil(raster, int(aux[i]))) for i in range(int(line[1]))))
            end = time.time()
            sys.stdout = open("resultscounting.txt", "a+")
            print(end-start)
        line = input().split()


if __name__ == "__main__":
    #func("qkdkq")
    n = 1
    while n < 11:
        func("random"+str(n*100000)+".txt")
        n+=1
    #l = [2,44,6,2,123,56,1,59]
    #radixSort(l)
    #print(l)

"""
def partition(arr, low, high):
    i = (low - 1)  # index of smaller element
    middle = int((high + low) / 2)
    if (arr[low]) > arr[middle]:
        arr[middle], arr[low] = arr[low], arr[middle]
    if (arr[low]) > arr[high]:
        arr[high], arr[low] = arr[low], arr[high]
    if (arr[middle]) > arr[high]:
        arr[high], arr[middle] = arr[middle], arr[high]
    pivot = arr[high]  # pivot

    for j in range(low, high):

        # If current element is smaller than or
        # equal to pivot
        if arr[j] <= pivot:
            # increment index of smaller element
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)

def insertion(raster, low, high):
    for i in range(low + 1, high):
        key = raster[i]
        j = i - 1
        while j >= 0 and key < raster[j]:
            raster[j + 1] = raster[j]
            j -= 1
        raster[j + 1] = key

def quickSort(arr, low, high):
    cutoff = 30
    if len(arr) == 1:
        return arr
    if low + cutoff > high:
        insertion(arr, low, high + 1)
    else:
        if low < high:
            # pi is partitioning index, arr[p] is now
            # at right place
            pi = partition(arr, low, high)

            quickSort(arr, low, pi - 1)
            quickSort(arr, pi + 1, high)
"""