""" Os elementos são inseridos sempre no final da fila, enquanto, para remover um elemento, é necessário fazê-lo pela frente da fila. O final de uma fila é aquele em que fica o último elemento inserido. Não temos como recuperar um elemento do meio da fila sem antes remover todos aqueles à sua frente. """

""" Manipulando os dados da fila
No exemplo a seguir, vamos iniciar uma fila vazia e utilizar os métodos append e pop para modificar nossa fila."""

print("\n_______________________\n")

fila = []
fila.append(1)
fila.append(2)
fila.append(3)
print(fila)
fila.append(4) # ← último elemento inserido
print(fila)
fila.pop(0) # ← retorna e remove o primeiro elemento
print(fila)
fila.pop() # ← retorna e remove o primeiro elemento, numero "2
print(fila)



print("\n_______________________\n")