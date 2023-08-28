# A estrutura while permite que um bloco de instruções seja repetido enquanto uma condição seja verdadeira.
#O laço while tem, em geral, o seguinte formato:
"""
while <condição>:
      Bloco que será repetido enquanto a condição for verdadeira
Instrução fora do while
"""
#exemplo:
palavra = input('Entre com uma palavra: ')
while palavra != 'sair':
    palavra = input('Digite sair para encerrar o laço: ')
print('Voce digitou sair e agora está fora do laço.')

"""
Considere que queremos saber depois de quantos anos uma aplicação, com juros anuais informados pelo usuário, terá atingido 50% de rendimento sobre o valor aplicado inicialmente. Ou seja, se a aplicação inicial foi de R$1.000,00, quantos anos serão necessários para atingir o valor de R$1.500,00?
ex:
"""
fator = 1
contador = 0
taxa = eval(input('Entre com a taxa de juros  anual em porcentagem: '))
while fator <1.5:
    fator += fator*taxa/100
    contador += 1
print(f'são necessários {contador} anos para atingir 50% de rentabilidade com  a taxa de {taxa}% ao ano') 

"""
outro exemplo:
"""
termo = soma = contador = 1
while termo >= 0.01:
    termo *= 0.5
    soma += termo
    contador += 1
print(f'A soma dos {contador} termos vale {soma}.')
print(f'o {contador+1}º termo vale {termo} e ficou abaixo de 0.01.')