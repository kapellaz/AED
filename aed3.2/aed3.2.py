import sys
import time
from matplotlib import pyplot as plt

class Node:
  def __init__(self, nome, hashh, oferta):
    self.nome = nome
    self.hashh = hashh
    self.oferta = oferta
    self.parent = None
    self.left = None
    self.right = None

class splayT:
  def __init__(self):
    self.root = None

  def esqRot(self, n):
    y = n.right
    n.right = y.left
    if y.left != None:
      y.left.parent = n

    y.parent = n.parent
    if n.parent == None: #n é a raiz
      self.root = y

    elif n == n.parent.left: #n é filho esquerdo
      n.parent.left = y

    else: #n é filho direito
      n.parent.right = y

    y.left = n
    n.parent = y

  def dirRot(self, n):
    y = n.left
    n.left = y.right
    if y.right != None:
      y.right.parent = n

    y.parent = n.parent
    if n.parent == None: #n é raiz
      self.root = y

    elif n == n.parent.right: #n é filho direito
      n.parent.right = y

    else: #n é filho esquerdo
      n.parent.left = y

    y.right = n
    n.parent = y

  def splay(self, n):
    while n.parent != None: #no nao é a raiz
      if n.parent == self.root: #se o no for filho da raiz só há uma rotacao
        if n == n.parent.left:
          self.dirRot(n.parent)
        else:
          self.esqRot(n.parent)

      else:
        p = n.parent #pai
        g = p.parent #avo

        if n.parent.left == n:
          if p.parent.left == p: #se sao dois esquerdos
            self.dirRot(g)
            self.dirRot(p)
          elif p.parent.right == p: #pai esquerdo avo direito
            self.dirRot(p)
            self.esqRot(g)
        elif n.parent.right == n:
          if p.parent.right == p: #se sao dois direitos
            self.esqRot(g)
            self.esqRot(p)
          elif p.parent.left == p: #pai direito avo esquerdo
            self.esqRot(p)
            self.dirRot(g)




  def insere(self, node):
    y = None
    temp = self.root
    while temp != None:
      y = temp
      if node.nome < temp.nome:
        temp = temp.left
      elif node.nome > temp.nome:
        temp = temp.right
      elif node.nome == temp.nome:
        print("ARTIGO JA EXISTENTE")
        return

    node.parent = y

    if y == None: #se o novo nó for a raiz
      self.root = node
    elif node.nome < y.nome:
      y.left = node
    else:
      y.right = node
    self.splay(node)
    print("NOVO ARTIGO INSERIDO")


  def pesquisa(self, nome, root):
    if root:
      if nome == root.nome:
        self.splay(root)
        return root
      elif nome < root.nome:
        return self.pesquisa(nome, root.left)
      elif nome > root.nome:
        return self.pesquisa(nome, root.right)
    else:
      return None


  def oferta(self, nome, root, offer):
    if nome == root.nome:
      root.oferta = offer
      print("OFERTA ATUALIZADA")
      self.splay(root)

    elif nome < root.nome:
      return self.oferta(nome,root.left, offer)
    elif nome > root.nome:
      return self.oferta(nome,root.right, offer)
    else:
      print("ARTIGO NAO REGISTADO")
      return


  def inorder(self, n):  #faz o print em ordem da árvore
    if n != None:
      self.inorder(n.left)
      print(n.nome+" "+n.hashh+" "+n.oferta)
      self.inorder(n.right)



def main(t):
  info = input().split()
  while (info[0] != "FIM"):
    if info[0] == "ARTIGO":
      node = Node(info[1], info[2], info[3])
      t.insere(node)

    elif info[0] == "OFERTA":
      t.oferta(info[1], t.root, info[2])

    elif info[0] == "CONSULTA":
      temp = t.pesquisa(info[1], t.root)
      if temp:
        print(temp.nome+" "+temp.hashh+" "+temp.oferta)
        print("FIM")
      else:
        print("ARTIGO NAO REGISTADO")
    elif info[0] == "LISTAGEM":
      t.inorder(t.root)
      print("FIM")

    elif info[0] == "APAGA":
      t.root = None
      print("CATALOGO APAGADO")

    info = input().split()

import numpy as np
sys.setrecursionlimit(8000)
if __name__ == '__main__':
  sys.stdout = open("out.txt", 'w')
  times = list()
  t = splayT()
  sys.stdin = open("teste" + str(3500) + ".txt", 'r')
  main(t)
  comp = 100
  while comp <=3500:
    sys.stdin=open("consulta"+str(comp)+".txt", 'r')
    start = time.time()
    main(t)
    end = time.time()
    times.append(end-start)
    comp+=100
  print(times)
  times = np.array(times)
  times=times*4000
  plt.plot(times)
  plt.show()
