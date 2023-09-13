"""Definindo uma tupla"""

# a.tupla=()        (vazia)
# b.tupla=(a,b,c)   (pode ser com parenteses, saparados por virguala)
# c.tupla= a,b,c    (pode ser sem parenteses, saparados por virgula )
# d.tupla=(a,)      (tupla de um elemento)

""" utilizando o construtor tuple(), que aceita como parâmetro outras coleções """

# tupla = tuple()
# tupla = tuple([1,2,3])
# tupla = tuple((1,2,3))

""" Assim como nas listas, os elementos de uma tupla em Python podem ser de diferentes tipos, incluindo outra tupla, como no exemplo a seguir, em que temos como elementos um número inteiro, uma string, uma lista e uma outra tupla. 
exemplo: """

# tupla = (1, 'Hello', [1, 2], (3,4))

""" Elas não podem ser alteradas durante a execução do programa

A forma de acessar um elemento da Tupla é igual à das listas: precisamos apenas do índice do elemento.
No exemplo adiante, vamos imprimir o valor do elemento na posição 2, lembrando que o primeiro elemento da tupla tem índice 0:  """
print("\n---------------------------\n")

tupla = ('a', 'b', 'c')
item = tupla[2]
print(item) #imprime o item "c")

print("\n---------------------------\n")



