
class TreeNode():
    def __init__(self, username):
        self.username=username
        self.ccInfo=dict()
        self.left=None
        self.right=None
        self.height=1

import sys



#funcao que acrescenta um nó
def acrescenta(root, username, creditCard, expiraDate):
    #procura a posicao para inserir o novo nó
    if not root:
        root = TreeNode(username)
        root.ccInfo[creditCard]=expiraDate
       # print("NOVO UTILIZADOR CRIADO")
        return root
    elif username < root.username:
        root.left = acrescenta(root.left, username, creditCard, expiraDate)
    elif username>root.username:
        root.right = acrescenta(root.right, username, creditCard, expiraDate)
    elif username==root.username:
        existe = False
        for k in root.ccInfo.keys():
            if k == creditCard:
                root.ccInfo[k] = expiraDate
                existe=True
               # print("CARTAO ATUALIZADO")
                break
        if(not existe):
            root.ccInfo[creditCard]=expiraDate
            #print("NOVO CARTAO INSERIDO")

    root.height = 1 + max(getHeight(root.left), getHeight(root.right))

    # Atualiza o fator de equilibrio
    fe = getFe(root)
    if fe > 1:
        if username < root.left.username:
            return rodaDir(root)
        else:
            root.left = rodaEsq(root.left)
            return rodaDir(root)

    if fe < -1:
        if username > root.right.username:
            return rodaEsq(root)
        else:
            root.right = rodaDir(root.right)
            return rodaEsq(root)

    return root


# rotacao à esquerda
def rodaEsq(z):
    y = z.right
    T2 = y.left
    y.left = z
    z.right = T2
    z.height = 1 + max(getHeight(z.left), getHeight(z.right))
    y.height = 1 + max(getHeight(y.left), getHeight(y.right))
    return y


# rotacao à direita
def rodaDir(z):
    y = z.left
    T3 = y.right
    y.right = z
    z.left = T3
    z.height = 1 + max(getHeight(z.left), getHeight(z.right))
    y.height = 1 + max(getHeight(y.left), getHeight(y.right))
    return y


# retorna o peso de um nó
def getHeight(root):
    if not root:
        return 0
    return root.height


# retorna o fator de equilibrio de um no
def getFe(root):
    if not root:
        return 0
    return getHeight(root.left) - getHeight(root.right)


# printa a informacao de um determinado utilizador
def consulta(root,usr):
    if root:
        if root.username==usr:
            #for k in sorted(root.ccInfo.keys()):
            #    print(str(k)+" " +str(root.ccInfo[k]))
            #print("FIM")
            return True
        return consulta(root.left, usr) or consulta(root.right, usr)




#print Inorder para imprimir por ordem lexicográfica
def printa(root):
    if root:
        printa(root.left)

        print(root.username+" " + " ".join(str(k) + " " + str(root.ccInfo[k]) for k in sorted(root.ccInfo.keys())))

        printa(root.right)


# lê os inputs e realiza as acoes pedidas
def main(root):
    info= input().split()
    while(info[0]!="FIM"):
        if info[0] == "ACRESCENTA":
            root = acrescenta(root, info[1], info[2], info[3])
        elif info[0] == "CONSULTA":
            if(not consulta(root, info[1])):
                pass
                #print("NAO ENCONTRADO")

        elif info[0] == "LISTAGEM":
           printa(root)
           #print("FIM")
        elif info[0] == "APAGA":
            root = None
            #print("LISTAGEM APAGADA")
        info = input().split()

import time
#import matplotlib.pyplot as plt


if __name__ == '__main__':
    aux = 50
    times = list()
    while aux <=100:
        sys.stdin = open("teste"+str(aux)+"0000.txt", 'r')
        start = time.time()
        root = None
        main(root)
        end = time.time()
        tempo = end-start
        print(tempo)
        times.append(tempo)
        aux+=5
    print(times)

