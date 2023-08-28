# Ao chamar o método range(), Python cria uma sequência de números inteiros. Ela pode ser chamada de maneira simples, apenas com um argumento. Nesse caso, a sequência começará em 0 e será incrementada de uma unidade, até o limite do parâmetro passado (exclusive). Por exemplo: 

range(3) # range(3) cria a sequência (0, 1, 2).

# Para que a sequência não comece em 0, podemos informar o início e o fim como parâmetros, lembrando que o parâmetro fim não entra na lista (exclusive o fim). O padrão é incrementar cada termo em uma unidade. Ex:

range(2,7) # range(2, 7) cria a sequência (2, 3, 4, 5, 6).

# Também é possível criar sequências mais complexas, indicando os parâmetros de início, fim e passo, nessa ordem. O passo é o valor que será incrementado de um termo para o próximo. Ex:

range(2,9,3) #  range(2, 9, 3) cria a sequência (2, 5, 8).
