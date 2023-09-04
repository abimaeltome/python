""" Definindo uma matriz"""

""" A declaração de matrizes é muito semelhante à de um vetor. Declaramos uma matriz de duas dimensões da seguinte forma: """

# nome = array([ [vetor1], [vetor2], [vetor3], ... ], dtype=tipo)

""" Nesse caso, nome é o nome da variável, vetor1, vetor2 e vetor3 representam as linhas da matriz e tipo é o tipo do elemento que será armazenado na matriz como int, float e str. O número de colunas será determinado pelo número de elementos dos vetores. """


print("\n\n\n----------------------------------------------------\n\n\n")

from numpy import array

materias = array ([["Português", "Matemática", "Química"], ["História", "Geografia", "Física"]], dtype=str)
print(materias[0][0])
print(materias[1][2])




print("\n\n\n\n----------------------------------------------------\n\n") 



""" Para alterar um elemento de uma matriz, basta atribuir o novo valor ao seu índice. No exemplo a seguir, vamos substituir o valor Física, que está no índice [1][2], por Cálculo: """


print("\n\n\n----------------------------------------------------\n\n\n")
# from numpy import array
# materias = array ([["Português", "Matemática", "Química"], ["História", "Geografia", "Física"]], dtype=str)
materias[1][2] = "Cálculo"
print(materias[1][2])


print("\n\n\n\n----------------------------------------------------\n\n") 