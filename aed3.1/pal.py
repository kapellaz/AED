with open("entradas.txt", 'w') as file_output:
    x10 = 900
    for i in range (x10):
        if i == 0 and x10 !=0:
            file_output.write("Todos 0 3\nArte 5 2\nClassica 1000 0\nFotografia 50 0\nLivros 100 0\nMusica 0 3\nRock 20 1\nSoftRock 5 0\nPop 20 0\nCountry 20 1")
        elif i != x10-1:
            file_output.write("\nTodos 0 3\nArte 5 2\nClassica 1000 0\nFotografia 50 0\nLivros 100 0\nMusica 0 3\nRock 20 1\nSoftRock 5 0\nPop 20 0\nCountry 20 1")
        else:
            file_output.write("\nTodos 0 3\nArte 5 2\nClassica 1000 0\nFotografia 50 0\nLivros 100 0\nMusica 0 3\nRock 20 1\nSoftRock 5 0\nPop 20 0\nCountry 20 0")

