idade = eval(input('Informe a idade da criança: '))
if idade < 5:
    print('A criança deve ser vacina contra gripe.')
    print('Procure um posto de saúde mais próximo.')
else:
    if idade == 5:
        print('A vacina estará disponível em breve.')
        print('Aguarde as próximas informações.')
    else:
        print('A vacinação só ocorrerá daqui a 3 meses.')
        print('Informe-se novamente neste prazo')
print('Cuide da saúde sempre! Até a próxima!')
