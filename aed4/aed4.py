import copy


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

def insertionSort(raster):
    aux = copy.deepcopy(raster)
    for i in range(1, len(aux)):
        key = aux[i]
        j = i - 1
        while j >= 0 and key < aux[j]:
            aux[j + 1] = aux[j]
            j -= 1
        aux[j + 1] = key
    return aux


import math


def mediana_elementar(raster):
    if len(raster) == 1:
        return raster[0]
    aux = insertionSort(raster)
    size = len(aux)
    if size % 2 == 0:
        return (aux[int(size / 2) - 1] + aux[int(size / 2)]) // 2
    else:
        return aux[math.ceil(size / 2)]


def percentil_elementar(raster, num):
    sorted_r = insertionSort(raster)
    inferiores = 0
    for i in sorted_r:
        if i < num:
            inferiores += 1
        else:
            break
    return int((inferiores / len(sorted_r)) * 100)


def amplitude_elementar(raster):
    if len(raster) == 1:
        return 0
    sorted_r = insertionSort(raster)
    return sorted_r[len(sorted_r) - 1] - sorted_r[0]


# ----------------------------------------------------------------------------------------------------------------------


def partition(raster, low, high):
    i = (low - 1)
    pivot = raster[high]

    for j in range(low, high):

        if raster[j] <= pivot:
            i = i + 1
            raster[i], raster[j] = raster[j], raster[i]

    raster[i + 1], raster[high] = raster[high], raster[i + 1]
    return (i + 1)


def quickSort(raster, low, high):
    if len(raster) == 1:
        return raster
    if low < high:
        pi = partition(raster, low, high)

        quickSort(raster, low, pi - 1)
        quickSort(raster, pi + 1, high)
    return raster


def percentil(raster, num):
    sorted_r = quickSort(copy.deepcopy(raster), 0, len(raster)-1)
    inferiores = 0
    for i in sorted_r:
        if i < num:
            inferiores += 1
        else:
            break
    return int((inferiores / len(sorted_r)) * 100)


def amplitude(raster):
    if len(raster) == 1:
        return 0
    sorted_r = quickSort(copy.deepcopy(raster), 0, len(raster) - 1)
    return sorted_r[len(sorted_r) - 1] - sorted_r[0]


def mediana(raster):
    if len(raster) == 1:
        return raster[0]
    aux = quickSort(copy.deepcopy(raster), 0, len(raster) - 1)
    size = len(aux)
    if size % 2 == 0:
        return (aux[int(size / 2) - 1] + aux[int(size / 2)]) // 2
    else:
        return aux[math.ceil(size / 2)]


#----------------------------------------------------------------------------------------------------------------------

def main():
    MAX_ELEV = 10000
    line = input().split()
    global linha, coluna
    raster = list()
    while line[0] != "TCHAU":
        if line[0] == "RASTER":
            linha = int(line[1])
            coluna = int(line[2])
            for i in range(linha):
                line = input().split()
                for j in range(coluna):
                    raster.append(int(line[j]))
            print("RASTER GUARDADO")
        elif line[0] == "AMPLITUDE":
            print(amplitude(raster))
        elif line[0] == "MEDIANA":
            print(mediana(raster))
        elif line[0] == "PERCENTIL":
            aux = input().split()
            print(' '.join(str(percentil(raster, int(aux[i]))) for i in range(int(line[1]))))
        line = input().split()


if __name__ == "__main__":
    main()
