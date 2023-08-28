# A estrutura for permite que um bloco de instruções seja repetido para todos os itens de uma sequência. O laço for tem, em geral, o seguinte formato:
"""
for <variável> in <sequência>:
     Bloco que será repetido para todos os itens da sequência
Instrução fora do for

"""
#  EX: imprimir todos os elementos de uma sequência criada com a chamada range().
for item in range(2,9,3):
    print(item)

#    exemplo do laço for com uma string.
nome = input('Entre com seu nome: ')
for letra in nome: 
    print(letra)
