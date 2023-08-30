"""
USO DO PARÂMETRO return
"""
# função sem o return
def somarDoisNumeros(a, b):
    soma = a + b

print(somarDoisNumeros(1, 3))  #  Chama a função e exibe "None" 

# função como return

def somarDoisNumeros(a, b):
    soma = a + b
    return soma

print(somarDoisNumeros(1, 3))  #  Chama a função e imprime o resultado
