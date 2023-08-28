"""
A instrução continue também atua sobre as repetições dos laços for e while, como a instrução break, mas ela não interrompe todas as repetições do laço. A instrução continue interrompe APENAS a iteração corrente, fazendo com que o laço passe para a próxima iteração.
exemplo:
"""
for num in range (1, 11):
    if num == 5:
        continue
    else:
        print(num)
print('Laço encerrado')

#Para ressaltar a diferença entre as instruções break e continue, vamos agora alterar a linha 3 do nosso programa, trocando a instrução continue pela instrução break. Veja a nova execução:

for num in range (1, 11):
    if num == 5:
        break
    else:
        print(num)
print('Laço encerrado')