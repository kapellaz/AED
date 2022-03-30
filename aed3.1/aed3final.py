def monta(l,i):
    categoria = input()
    cat = categoria.split(" ")
    cat[1] = int(cat[1])
    cat[2] = int(cat[2])
    control = int(cat[2])
    cat.append(i)
    l.append(cat)
    while control != 0:
        l, v= monta(l, i+1)
        cat[1]+=v
        control -= 1
    return l, cat[1]


def imprime(l):
    max = 0
    for i in l:
        if i[3]>max:
            max = i[3]
    control = 1
    while control<=max:
        string = ' '.join(str(i[0]+'('+str(i[1])+')') for i in l if i[3]==control)
        control+=1
        print(string)


def main():
    l = list()
    monta(l, 1)
    imprime(l)


main()