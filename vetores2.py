""" Iterando o Vetor

Para percorrer um vetor, utiliza-se a sintaxe: """

# for elemento in vetor:
# ....(código)

""" Nesse caso, elemento é o nome da variável que conterá o valor de cada elemento; vetor, o nome da variável que desejamos percorrer; e (código), o trecho de código que será repetido pelo laço. Veja o exemplo a seguir. Nele, vamos imprimir todos os elementos do vetor notas_real. """

print("\n\n\n-----------------------INÍCIO---------------------------\n\n\n")




from numpy import array
notas_real = array([2, 5, 10, 20, 50, 100], dtype=int)

for elemento in notas_real:
    print(elemento, end=" - ")





print("\n\n\n\n-----------------------FIM------------------------------\n\n") 



