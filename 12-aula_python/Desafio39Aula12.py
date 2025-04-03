ano = int(input('Digite o seu ano de nascimento '))
data = 2025 - ano
data2 = 18 - data

if data == 18:
    print('Você tem que servir esse ano!!!')

elif data > 18:
    print('Você está atrasado!!')


elif data2 < 18:
    print('Você ainda vai se alistar, Falta apenas, {} Ano para o alistamento!!!'.format (data2))
 




