print('='*40)
print('CADASTRE UMA PESSOA')
print('='*40)

contador, maioridade, mulher20anos, masculino = 0, 0, 0, 0
continuar = ' '

while continuar not in'N':
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo [F/M]: ').strip().upper()
    print('='*40)
    continuar = str(input('Quer continuar? [S/N]')).strip().upper()
    print('='*40)
    if continuar == 'Nn':
        break

    elif idade >= 18 and sexo == 'M':
        maioridade +=1
        masculino +=1
    elif sexo == 'F' and idade <= 20:
        mulher20anos +=1
print(f'Total de pessoas com mais de 18 anos é {maioridade}\n'
      f'Ao todo temos {masculino} homens cadastrados.\n'
      f'E temos {mulher20anos} com menos de 20 anos.')