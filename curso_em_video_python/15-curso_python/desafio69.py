idade = 0
sexo = ' '
enfeite = '-'*40
maior = 0
homem = 0
mulher = 0
while True :
    print(f'{enfeite} PESSOA {enfeite}')
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo: [F/M] ')).upper()
    if idade > 18:
        maior+=1
    if sexo in 'Mm':
        homem+=1
    if sexo in 'Ff' and idade > 20:
        mulher +=1
    print('Quer continuar? ')
    print('[1] Sim')
    print('[2] Não')
    simOuNao = int(input('Digite o número correspondido com sua resposta: '))
    if simOuNao == 1:
        print ('Continuando...')
    else :
        print('FINALIZANDO...')
        break
print (f'O total de maiores de 18 anos foi {maior}.')
print(f'A quantidade de homens foi {homem}.')
print(f'A quantidade de mulheres maiores de 20 é {mulher}')