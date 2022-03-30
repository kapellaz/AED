import time
import sys


sys.setrecursionlimit(10**9)


class Node:

    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor
        self.child = []

def monta(f):
    categoria = f.readline()
    cat = categoria.split(" ")
    raiz = Node(cat[0], int(cat[1]))
    control = int(cat[2])
    while control != 0:
        son = monta(f)
        raiz.child.append(son)
        raiz.valor += son.valor
        control -= 1

    return raiz

def tree():
    with open("entradas.txt", 'r') as f:
        raiz = monta(f)
    f.close()
    return raiz

def imprime(root):
    q = [] #fila de espera para a impressao
    q.append(root)
    while (len(q) != 0):
        n = len(q)
        #Se o no tiver filhos
        while (n > 0):
            p = q[0]  #guarda a informacao do pai
            q.pop(0)  #remove o pai da fila de espera
            if(n>1):
                print(p.nome+'('+str(p.valor)+')', end=' ')
            else:
                print(p.nome + '(' + str(p.valor) + ')', end='')

            #adiciona os filhos à lista de espera
            for i in range(len(p.child)):
                q.append(p.child[i])
            n -= 1
        print()

l = list()
media=0
for i in range(20):
    start = time.time()
    raiz= tree()
    end = time.time()
    tempo = end-start
    media+=tempo
    l.append(tempo)

print(l)
print(media/20)
imprime(raiz)
