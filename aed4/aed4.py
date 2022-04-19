
def amplitude(raster):
    max = 0
    min=100000
    for i in raster:
        if i>=max:
            max = i
        if i <=min:
            min = i
    return max-min


def percentil(raster, num):
    size = 0
    inferiores = 0
    for i in raster:
        if i < num:
            inferiores+=1
        size+=1
    return int((inferiores/size)*100)

def percentil_elementar(raster):
    pass

def percentil_quick(raster):
    pass

def percentil_linear(raster):
    pass



def mediana(raster):
    size = len(raster)
    soma = 0
    if size == 1:
        return raster[0]
    for i in range(size):
        count = 0
        numberof=0
        for j in range(size):
            if raster[i]>raster[j]:
                count+=1
            if raster[i] == raster[j]:
                numberof += 1

        if count < (size / 2) and count+numberof>=size/2 and soma==0:
            if size%2!=0:
                return raster[i]
            soma += raster[i]
        if count < (size / 2) + 1 and count+numberof>=size/2+1 and soma > 0:
            return (raster[i] + soma) // 2








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