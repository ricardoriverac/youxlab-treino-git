sexo= ''
count= 0
maiores= 0
homens= ''
mulheres= ''
escolha= ''
idade= 0
print('Olá! Quero conhecer melhor você.')
while True:
    sexo= input('Qual é o seu sexo?: ') .upper() .capitalize()
    idade= int(input('Qual a sua idade?: '))
    if sexo == 'F':
        mulheres= sexo
        print(f'Sua idade é {idade} e seu sexo é feminino. Que legal!')
        escolha= input('Você deseja continuar? [sim/não]: ') .upper() .capitalize()
        if sexo == 'F':
            mulheres= sexo
            count +=1
            if count != 1:
                print(f'{count} mulheres tem menos de 20 anos.')
            if count == 1:
                print(f'Apenas {count} mulher tem menos de 20 anos.')

    if sexo == 'M':
        homens= sexo
        print(f'Sua idade é {idade} e seu sexo é masculino. Que legal!')
        escolha= input('Você deseja continuar? [sim/não]: ') .upper() .capitalize()
        if sexo == 'M':
            homens= sexo
            count+=1
            if count != 1:
                print(f'{count} homens foram cadastrados.')
            if count == 1:
                print(f'Apenas {count} homem foi cadastrado.')
    if escolha == 'N':
        if idade >= 18:
            maiores= idade
            count +=1
            print(f'{count} pessoas são maiores de idade.')
            if count == 1:
                 print(f'Apenas {count} pessoa é maior de 18 anos.')
        break       

    

    

