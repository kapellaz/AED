import random
import sys

import numpy as np



aux = 100
maxi=4000
comp = aux
while comp <=maxi:
    sys.stdout=open("teste"+str(comp)+".txt", 'w')

    i = 0
    for j in range(comp):
        print("ARTIGO " + "Pintura"+str(i) + " "+str(np.random.randint(1000,9999)) + " "+str(np.random.randint(100,999)))
        i+=1

    print("FIM")
    comp+=aux

comp = aux
while comp <=maxi:
    consultas = np.random.choice(comp, int(comp*0.05), replace=False)
    outros = [i for i in range(comp) if i not in consultas]
    consultas=list(consultas)
    teste=[]

    for i in range(int((comp*0.90)/len(consultas))):
        for j in consultas:
            teste.append(j)

    random.shuffle(outros)
    for p in range(comp-len(teste)):
        teste.append(outros[p])

    random.shuffle(teste)
    sys.stdout = open("consulta" + str(comp) + ".txt", 'w')
    for j in range(len(teste)):
        print("CONSULTA " + "Pintura"+str(teste[j]))
    print("FIM")
    comp+=aux





comp = aux
while comp <=maxi:
    teste = [i for i in range(comp)]
    random.shuffle(teste)
    sys.stdout = open("1consulta" + str(comp) + ".txt", 'w')
    for j in range(len(teste)):
        print("CONSULTA " + "Pintura"+str(teste[j]))
    print("FIM")
    comp+=aux





