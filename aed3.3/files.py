import random
import sys

import numpy as np


comp = 500000
while comp <=1000000:
    sys.stdout=open("teste"+str(comp)+".txt", 'w')
    randnums= np.random.randint(1000000,9999999,int(comp*0.90))
    randexp= np.random.randint(1000,9999,int(comp*0.90))

    for j in range(50):
            for i in range(int(len(randnums)/50)):
                    print("ACRESCENTA " + str(j) + " "+str(randnums[i]) + " "+str(randexp[i]))


    randcons = np.random.randint(0,50, int(comp*0.10))
    for i in randcons:
        print("CONSULTA " + str(i))

    print("FIM")
    comp+=50000