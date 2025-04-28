genero = str(input('Digite o seu sexo:[M/F] ')).upper().strip()[0]
if genero == 'M' :
        print('Olá, senhorito.')
elif genero == 'F' :
        print('Olá, senhorita.')
     
while genero not in 'MmFf':
    genero= str(input('Você digitou algo errado, tente novamente: ')).upper().strip()[0]
print('Cadastro feito.')
     
        