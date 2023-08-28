#Suponhamos que seja preciso imprimir todos os números inteiros de 1 a 10, informando a paridade de cada um deles.
"""
Para isso, temos que usar a estrutura de repetição (para que os números variem de 1 a 10) e a estrutura de decisão (para testar se o número é par ou ímpar). Ou seja, podemos usar o laço for em conjunto com a estrutura if (ou if-else). EX:
"""
for num in range(1,11): 
    if num % 2 == 0: 
        print(f'{num} é par')
    else:
        print(f'{num} é ímpar')

  #      OPERAÇÕES ARITMÉTICAS COM INTEIROS – USO DO for COM ACUMULADOR E CONTADOR

#ex acumulador 
soma = 0
limite = eval(input('Entre com um número inteiro positivo: '))
for num in range(1, limite+1):
    soma += num
print(f'A soma dos inteiros de 1 até {limite} vale {soma}') 

# ex contador
soma = contador = 0
limite = eval(input('Entre com um número inteiro positivo: '))
for num in range(1, limite+1):
    soma += num
    contador += 1
print(f'A média dos inteiros de 1 até {limite} vale {soma/contador}')

#USO DO LAÇO for COM QUALQUER SEQUÊNCIA
nomes = ['luara', 'lis', 'guilherme', 'enzo', 'izabel']
for nome in nomes:
    print(nome)


