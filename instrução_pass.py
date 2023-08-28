#A instrução pass atua sobre a estrutura if, permitindo que ela seja escrita sem outras instruções a serem executadas caso a condição seja verdadeira.
for num in range(1, 11):
    if num % 2 == 0:
        pass
    else:
        print(num)
print('Laço encerrado. ')