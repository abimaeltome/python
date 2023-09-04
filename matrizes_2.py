""" Iterando a matriz 
Para percorrer os elementos de uma matriz de duas dimensões, utiliza-se a sintaxe: """
# for linha in matriz:
#     for elemento in linha:
#          ....(código)
""" Veja o exemplo a seguir. A função itera_matriz imprime todos os elementos da matriz recebida por parâmetro: """

print("\n\n----------------------------------------------------\n\n")

from numpy import array


def itera_matriz(matriz):
    for linha in matriz:
        print("Início de uma nova linha")
        for elemento in linha:
            print(elemento)

def altera_matriz(matriz, elemento, i, j):
    matriz[i][j] = elemento
    return matriz

def main():
    matriz = array([["Português", "Matemática", "Química"], ["História", "Geografia", "Física"]], dtype=str)   
    matriz = altera_matriz(matriz, "biologia", [1],[0])
    itera_matriz(matriz)
    

    

    
if __name__ == "__main__":
    main()


print("\n\n\n----------------------------------------------------\n\n") 
