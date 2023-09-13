""" As operações de inserção e remoção de um item na pilha são normalmente chamadas de push e pop. Elas fazem as seguintes inserções: push (Insere um item no topo da pilha) e pop (Remove o item do top da pilha)"""

#Append ( insere o item no final da lista. Ele faz o papel do push)
#Pop ( Esse método retorna e remove o último elemento da lista. Ele faz o papel do próprio pop.)

""" Manipulando os dados da pilha """

"""No exemplo adiante, vamos iniciar uma pilha vazia e utilizar os métodos append e pop para modificá-la: """
print("\n___________________________\n")
      
pilha = []
pilha.append(1)
pilha.append(2)
pilha.append(3)
print(pilha)
pilha.append(4) # ←  útimo elemento inserido
print(pilha)


print("\n___________________________\n")

pilha.pop() # ← retorna e remove o último elemento "4"
print(pilha) #  o 3 passa a ser o último elemento
pilha.pop() # ← retorna e remove o último elemento "3"
print(pilha)#  o 2 passa a ser o último elemento
pilha.pop()# ← retorna e remove o último elemento "2"
print(pilha) #  o 1 passa a ser o último elemento