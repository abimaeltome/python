""" Para definirmos um vetor em NumPy, utilizamos a seguinte sintaxe: """

# nome = array([ elementos ], dtype=tipo)

""" Nesse caso, nome é o nome da variável; elementos, os itens separados por vírgula que vão compor o vetor; e tipo, o tipo do elemento que será armazenado no vetor como int, float e str. O tamanho do vetor é definido automaticamente pelo número de elementos.

Para ilustrarmos isso, vamos declarar uma variável chamada notas_real, que é um vetor de inteiros contendo os seis possíveis valores de notas do Real: R$2,00, R$5,00, R$10,00, R$20,00, R$50,00 e R$100,00. Primeiramente, vamos importar a classe array do NumPy e, em seguida, declarar o vetor. """

print("----------------------------------------------------------------")


from numpy import array
notas_real = array([2, 5, 10, 20, 50, 100], dtype=int)




""" Em NumPy, podemos acessar um elemento de um vetor da seguinte forma: """

# nome[indice]

""" Nesse caso, indice é um número inteiro que representa a posição do elemento no vetor. Em NumPy, o índice começa em 0 (zero) 

Este código imprime os dados armazenados nos índices 0 e 5: """

notas_real = array([2, 5, 10, 20, 50, 100], dtype = int)
print(notas_real[0])
print(notas_real[5])


print("----------------------------------------------------------------")

"""Para alterar um elemento do vetor, basta atribuir o novo valor ao seu índice. Vamos praticar isso um pouco:"""


print("----------------------------------------------------------------")


from numpy import array

def main():
    idades = array([10, 30, 45, 62, 74], dtype=int)
    print(f"vetor antes da insercao: {idades}")
    indice = eval(input("informe o índice do vetor ")) # recebe o índice
    elemento = eval(input("informe o elemento do vetor ")) # recebe o novo elemento
    # inserindo o novo elemento escolhido
    idades[indice] = elemento
    print(f"vetor depois da insercao: {idades}")

# Teste lógico __name__ == "__main__" 
# __name__ é uma variável especial do Python 
# __name__ terá o valor  “__main__” quando o script é executado diretamente 
# (nosso caso, quando o botão Executar do emulador for pressionado)
# __name__ terá como valor o nome do script (sem o .py) em caso de importação do script como módulo por um outro script
if __name__ == "__main__":
    main()

print("----------------------------------------------------------------")

""" Iterando o Vetor

Para percorrer um vetor, utiliza-se a sintaxe: """

# for elemento in vetor:
# ....(código)

""" Nesse caso, elemento é o nome da variável que conterá o valor de cada elemento; vetor, o nome da variável que desejamos percorrer; e (código), o trecho de código que será repetido pelo laço. Veja o exemplo a seguir. Nele, vamos imprimir todos os elementos do vetor notas_real. """

print("----------------------------------------------------------------")


for elemento in notas_real:
    print(elemento, end=" - ")


print("----------------------------------------------------------------")
