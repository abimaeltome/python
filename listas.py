""" DEFININDO UMA LISTA"""

""" Para declararmos um objeto do tipo list, podemos proceder de diversas formas: """

""" utilizar apenas os conchetes para declarar uma lista vazia  """
# lista = [] 

""" utilizar os conchetos com os elementos separados por vírgula"""
# lista =  [a, b, c]

""" Utilizar o construtor list(), que aceita como parâmetros outras coleções """
# lista = list()
# lista = list([1,2,3])

""" ACESSANDO OS DADOS DA LISTA """

""" A forma de acessar um elemento da lista é muito similar à das matrizes. Precisa-se apenas do índice do elemento.

No exemplo a seguir, vamos imprimir o valor do elemento na posição 1, lembrando que o primeiro elemento da lista tem índice 0 . """

# >>> lista = ['a', 'b', 'c', 'b']
# >>> item = lista[1]
# >>> print(item)
# 'b'

""" Durante a programação, é comum não saber o índice do elemento que se deseja acessar. Para esse tipo de situação, pode-se utilizar o método index, que retorna o índice do elemento procurado.

Observe que o método index retorna o índice da primeira ocorrência do elemento. """
print("\n\n-------inicio----------\n\n")

lista = ['a', 'b','c', 'd']
indice_c = lista.index('c')
print(indice_c)

print("\n\n--------fim---------\n\n")
print("\n\n--------inicio-------\n\n")

indice_b = lista.index('b')
print(indice_b)


print("\n\n--------fim-------\n\n")

print("\n\n--------inicio-------\n\n")


"""Assim como nas matrizes, podemos utilizar o índice de um elemento para alterá-lo.

No exemplo a seguir, recuperaremos o índice da palavra carro e o alteraremos para moto:"""

lista1 = ["avião", "helicóptero", "carro", "navio"]
indice_carro = lista1.index("carro")
print(indice_carro)

lista1[indice_carro] = "moto" # Alteração do elemento na posição de índice 2 da lista
print(lista1)


print("\n\n---------fim--------\n\n")
