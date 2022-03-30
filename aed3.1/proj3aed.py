

def monta(d,i):
    linha_da_arvore = i
    categoria = input()
    cat = categoria.split(" ")

    if cat[0] not in d:
        d[cat[0]] = [int(cat[1]), int(cat[2])]

    d[cat[0]].append(linha_da_arvore)
    control = int(cat[2])
    while control!=0:
        d[cat[0]][0]+=monta(d, i+1)
        control-=1
    return int(d[cat[0]][0])




def main():
    d = dict()
    monta(d, 1)
    max = 0
    for k in d.keys():
        if d[k][2]>max:
            max = d[k][2]
    control = 1
    while control <= max:
        string = " ".join(str(k)+"("+str(d[k][0])+") " for k in d.keys() if d[k][2] == control)
        print(string[:-1])
        control+=1

main()
