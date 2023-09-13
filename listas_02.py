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
lista.append("carro") # append, insere 'carro' no final da lista
print(lista)
lista.append("moto")
lista.append("avião")
print(lista)
lista.insert(1, "bicicleta") # Inserimos o elemento bicicleta na posição de índice 1
print(lista)

print("\n________________________\n")



""""Em algumas ocasiões, precisamos juntar duas listas. Para isso, usamos o método extend, em que passamos uma lista como parâmetro. Também podemos empregar o método append, porém, para isso, teríamos de adicionar uma lista dentro da outra, que não é o desejado.  exemplo"""

print("\n________________________\n")


lista_a = [1,2,3]
lista_b = [4,5,6]
lista_a.append(lista_b) # lista_b foi adicionada dentro da lista_a como um elemento único
print(lista_a)


print("\n________________________\n")
print("________________________")

lista_a = [1,2,3]
lista_a.extend(lista_b) # lista_a e lista_b foram concatenadas
print(lista_a)


print("\n________________________\n")
""" Além dos métodos para adicionar elementos, o list contém aqueles usados para remover itens da lista. O método remove é utilizado para tirar o elemento passado como parâmetro, enquanto o clear remove todos os elementos da lista.

Observe, no exemplo a seguir, que, para usarmos o método remove, não utilizaremos o índice, e sim o valor do elemento: """
print("\n________________________\n")


lista = ['carro','bicicleta', 'moto', 'avião']
lista.remove('bicicleta') # remevo, retira o item 'bicicleta' da lista
print(lista)

print("\n________________________\n")
print("________________________")


lista.clear() # clear, limpa a lista
print(lista)


print("\n________________________\n")

"""Outras funções da lista"""
""" lém dos métodos apresentados anteriormente, o objeto list contém outros que são úteis. Dois exemplos são o método sort, para ordenar a lista, e o reverse, para inverter os elementos dela. Ambos alteram a própria lista!

No próximo exemplo, mostraremos como esses métodos são utilizados: """
print("\n________________________\n")

lista_alfa = [3, 2, 1, 6, 9]
lista_alfa.sort() # sort, ordena a lista
print(lista_alfa)

print("\n________________________\n")
print("\n________________________\n")

lista_alfa.reverse() # reverse, inverte os elementos da lista
print(lista_alfa)


print("\n________________________\n")

"""Algumas funções internas do Python podem ser aplicadas às listas, como len, min, max e sum, que retornam o tamanho, o elemento de valor mínimo, o elemento de valor máximo e a soma dos elementos da lista, respectivamente.
exemplo:  """
print("\n________________________\n")
print(len(lista_alfa)) # len, mostra a quantidade de elementos da lista
print("\n________________________\n")
print(min(lista_alfa)) # min, mostra o elemento de valor mínimo
print("\n________________________\n")
print(max(lista_alfa)) # max,  min, mostra o elemento de valor máximo
print("\n________________________\n")
print(sum(lista_alfa)) # sum, soma os elemento da lista
print("\n________________________\n")

"""Também podemos combinar essas funções para alcançar novos objetivos. No exemplo adiante, vamos calcular a média dos números de uma lista sem percorrê-la apenas utilizando as funções sum e len:"""
print("\n________________________\n")

media = sum(lista_alfa)/len(lista_alfa)
print(media)


print("\n________________________\n")

""" OPERADORES NAS LISTAS """

""" Alguns operadores do Python, como os de pertinência (in e not in), equivalência (==), concatenação (+) e multiplicação (*), também podem ser aplicados aos objetos do tipo list. """

print("\n________________________\n")

lista_c = [1, 2, 3]
lista_d = [1, 2, 3]
lista_e = [4, 5, 6]
print(lista_c == lista_d) 


print("\n________________________\n")
print("\n________________________\n")

print(lista_c == lista_e)


print("\n________________________\n")
print("\n________________________\n")

if 3 in lista_c:
    print('achei o 3 !!!')

print("\n________________________\n")
print("\n________________________\n")

nova_lista = lista_c + lista_e
print(nova_lista)

print("\n________________________\n")
print("\n________________________\n")

lista_repetida = lista_c * 4
print(lista_repetida)

print("\n________________________\n")

"""Mais sobre as listas
Uma funcionalidade muito interessante e útil que o Python disponibiliza é a capacidade de criar listas e partir de outras listas de forma simplificada utilizando a chamada compreensão de listas (do inglês list comprehensions).

A compreensão de listas permite filtrar, transformar e aplicar funções aos elementos de uma lista. Sua sintaxe é:"""

# [item for item in lista]

""" Nesse caso, item é o nome da variável que receberá o valor de cada elemento da lista. É sobre essa variável que aplicaremos os filtros e as transformações.

No exemplo a seguir, desejamos multiplicar todos os itens de uma lista por 2: """
print("\n________________________\n")

lista_f = [1, 2, 3]
n_lista = [item*2 for item in lista_f]
print(n_lista)

print("\n________________________\n")

""" Para adicionarmos um filtro, colocaremos a condicionante if após a lista. Sua sintaxe será: """

# [item for item in lista if item cond]

""" Nesse caso, cond é uma condicionante. Por exemplo: item > 0, item == 'a', item.startswith('b') etc.

No exemplo adiante, vamos filtrar apenas os elementos pares de uma lista, ou seja, cujo resto da divisão por dois seja zero (%2 == 0): """
print("\n________________________\n")

lista_g = [0, 1, 2, 3, 4, 5, 6]
nov_lista = [item for item in lista_g if item%2 == 0] 
print(nov_lista)

print("\n________________________\n")

""" Criando cópias de listas (Shallow Copy versus Deep Copy) """

""" A Shallow Copy (Cópia superficial) cria uma um objeto novo e independente com o mesmo conteúdo"""

print("\n________________________\n")

lista_x = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]]]
lista_y = list(lista_x) # fazendo uma cópia superficial

""" A lista_y agora tem o mesmo conteúdo que a lista_x e pode ser alterada sem que essa alteração afete o conteúdo da lista original ex: entretanto se alterarmos a lista original(lista_x) a lista_y também será modificada """

lista_y.append('novo item')
print(lista_y) # a lista_y será mostrada com alterações
print(lista_x) # a lista_x será mostrada sem alterações

print("\n________________________\n")
print("\n________________________\n")

""" A Depp Copy (Cópia profunda) cria uma lista nova e independente com o mesmo conteúdo da lista original, porém dessa vez se alterarmos a lista original a nova lista não sofre alterações. exemplo: """

import copy # importa a função copy

lista_x = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]]]
new_lista = copy.deepcopy(lista_x) # copy.deepcopy, realizando a cópia profunda da lista_x
lista_x.append("novo numero") # alterando a lista original
print(new_lista) # a new_lista será mostrada sem alterações
print(lista_x) # a lista_x será mostrada com alterações



print("\n________________________\n")














