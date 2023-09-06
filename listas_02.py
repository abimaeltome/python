""" Alterando a lista """

""" Quando precisamos inserir um novo elemento na lista, podemos utilizar os métodos append ou insert. Esses métodos executam as inserções da seguinte forma:
"""

#append
""" O método append insere o elemento passado como parâmetro no final da lista """

#insert
""" O método insert insere o elemento na posição indicada no parâmetro. 
exemplo: """

print("\n________________________\n")


lista = list()
lista.append("carro")
print(lista)
lista.append("moto")
lista.append("avião")
print(lista)
lista.insert(1, "bicicleta") #Inserimos o elemento bicicleta na posição de índice 1
print(lista)

print("\n________________________\n")



""""Em algumas ocasiões, precisamos juntar duas listas. Para isso, usamos o método extend, em que passamos uma lista como parâmetro. Também podemos empregar o método append, porém, para isso, teríamos de adicionar uma lista dentro da outra, que não é o desejado.  exemplo"""

print("\n________________________\n")


lista_a = [1,2,3]
lista_b = [4,5,6]
lista_a.append(lista_b) # lista_b foi adicionada dentro da lista_a como um elemento único
print(lista_a)

print("\n________________________\n")