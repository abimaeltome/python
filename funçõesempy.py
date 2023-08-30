#como definifinar uma função sem parâmentro

"""
def nome(): 
    linha1
    linha2
    linha..
    ....   
    linhaN
(4 espaços)    
"""
#exemplo

def hello():
    print('Olá')
    print('Mundo')
#inicio do programa
print('incício do programa')
hello()
print('término do programa')

"""///////////////////////////////////////////////////////////////////////////////////////"""
#como definir uma função com parâmetros

"""
def nome(param1, param2,..): 
    linha1
    linha2
    linha..
    ....   
    linhaN
(4 espaços)   
"""
#exemplo:
def calcula_imc(peso, altura):
    print("Parametro peso:", peso)
    print("Parametro altura:", altura)
    imc=peso/altura**2
    print('IMC', imc)
#inicio do programa
print('Início do Programa')
calcula_imc(70, 1.88)
print("Término do Programa")
"""/////////////////////////////////////////////////////////////////////"""

#Como receber os resultados de uma função
def calcula_imc(peso, altura):
    print("Parâmetro peso", peso)
    print("Parâmetro altura", altura)
    imc = peso/altura**2
    return imc

#incício do programa
print("início do programa")
indice = calcula_imc(altura=1.8, peso=97)
print("IMC ", indice)
if indice <18.5:
    print("Baixo peso ")
elif indice <25:
    print("Peso adequado")
elif indice <30:
    print("Sobrepeso")
else:
    print("obeso")
print("Término do programa")
