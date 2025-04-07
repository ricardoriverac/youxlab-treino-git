flag = False

while flag == False:
    sexo = str(input('Informe seu sexo [M/F]: ')).upper().strip()
    if sexo == 'M' or sexo == 'F':
        flag = True
    else:
        print('Dados inválidos. Digite novamente!')
        flag = False
print(f'Sexo {sexo} registrado com sucesso')