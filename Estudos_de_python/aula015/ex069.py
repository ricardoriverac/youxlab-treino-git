print(' ')
print('-'*20)
print('CADASTRE UMA PESSOA ')
print('-'*20)
print(' ')

menorIdade =1
mulherMenor=1
homens=1

while True:

    idade=int(input('Idade: '))
    sexo =str(input('Sexo[M/F]: '))

    print(' ')

    escolha=(input('Quer continuar? [S/N]')).upper()

    if escolha == 'N':
        break

    if sexo == 'M': 
        homens += 1
    
    elif sexo == 'F' and idade < 20:
        mulherMenor += 1

    elif idade <= 20:
        menorIdade += 1

print(f'Ao todo temos {homens} homens')

print(f'O número de menores de idade e {menorIdade}')

print(f'E temos {mulherMenor} mulheres com menos de vinte anos:')


    





    








