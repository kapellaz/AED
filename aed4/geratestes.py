

import random
def gera(n):
    with open("random"+str(n)+".txt", 'w') as f:
        f.write("RASTER " + str(n) +" 1\n")
        numbers = [str(random.randint(0,10000)) for i in range(n)]
        random.shuffle(numbers)
        for i in numbers:
            f.write(str(i)+"\n")
        f.write("PERCENTIL "+str(n)+"\n")
        out= ' '.join(str(random.randint(0,10000)) for i in range(n))
        out+="\n"
        f.write(out)
        f.write("TCHAU\n")



#for i in range(1,11):
#    gera(i*100000)

gera(10)