print('-='*20)
print('{:^30}'.format('\033[1;35mCAIXA ELETRÔNICO\033[m'))
print('-='*20)
valor = int(input('Que valor você quer sacar? R$'))

while True:
    if valor == 0:
        print('Programa encerrado! Volte sempre! ')
        break
    if valor < 0:
        print("Valor inválido. Digite um valor positivo.\n")
        continue
    
    cedulas = [200, 100, 50, 20, 1]
    

    print('{:^30}'.format('\033[36mCédulas prontas:\033[m'))
    for cedula in cedulas:
        quantidade = valor//cedula
        valor = valor % cedula
        if quantidade > 0:
            print(f'{quantidade} cédula(s) de R${cedula}')
    
    
    
    
    

    # for cedula in cedulas:
    #     quantidade = valor // cedula  # Divide o valor pela cédula para saber quantas
    #     valor = valor % cedula        # Atualiza o valor restante
    #     if quantidade > 0:
    #         print(f"{quantidade} cédula(s) de R$ {cedula}")
    
    # print("") 
