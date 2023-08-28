
#O comando “assert” verifica se a condição é verdadeira. Se a condição for avaliada como falsa, uma exceção AssertionError será lançada com a mensagem de erro especificada.

lista = [5,10,20]
soma = sum(lista)
assert soma == 35, "A soma está incorreta"
assert soma != 35, "A soma está correta"
