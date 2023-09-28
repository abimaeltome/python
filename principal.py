"""Importação de um módulo
Para utilizar esse módulo em outro script, precisamos informar ao Python que queremos importá-lo. Uma das sintaxes para importar um módulo em Python é:
>>> import nome_arquivo
"""
#Utilizamos a palavra reservada import seguida do nome do arquivo SEM a extensão py. Para importar o módulo imc.py, fica assim:

import imc

"""
Utilização das definições de um módulo
No próximo exemplo, daremos um passo adiante. Mostraremos como utilizar a função calcula_imc definida dentro do módulo imc.

Para utilizar uma função definida em outro módulo, usamos a sintaxe:
>>> nome_modulo.nome_funcao(...)

Assim  temos o nome do módulo importado, seguido de um ponto e o nome da função. Para utilizar a função calcula_imc, temos:
>>> imc.calcula_imc(x, y)
"""
print("Início do programa")
indice = imc.calcula_imc(altura=1.80, peso=70)
print("IMC:", indice)
if indice < 18.5:
    print("Baixo peso")
elif indice < 25:
    print("Peso adequado")
elif indice < 30:
    print("Sobrepeso")
else:
    print("Obeso")
print("Fim do Programa")

"""
O Python também permite que o programador importe apenas a função desejada, sem a necessidade de importar o módulo todo. A sintaxe para isso é:

>>> from nome_modulo import nome_funcao
"""


