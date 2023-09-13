from collections import namedtuple

# Definindo a tupla nomeada
Pessoa = namedtuple('Pessoa', ['nome', 'idade', 'cidade'])

# Criando uma instância da tupla nomeada
p1 = Pessoa('João', 25, 'São Paulo')

# Acessando os campos da tupla nomeada
print(p1.nome)   # Saída: João
print(p1.idade)  # Saída: 25
print(p1.cidade) # Saída: São Paulo
