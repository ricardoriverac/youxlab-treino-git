from time import sleep
print('\033[1;35mVAMOS FAZER UMA MATRIZ\033[m')
sleep(1)
listaPrimeiraLinha = list()
listaSegundaLinha = list()
listaTerceiraLinha = list()
valoresPares = list()

print('\033[3;35mVALORES PRIMEIRA LINHA\033[m')
sleep(0.5)
for valores1 in range(1,4):
    valor = int(input(f'Digite o \033[1;35m{valores1}°\033[m valor da matriz: ')) 
    if valor %2 ==0:
        valoresPares.append(valor)
    listaPrimeiraLinha.append(valor)
listaPrimeiraLinha = [[x] for x in listaPrimeiraLinha]
print('-' * 40)
sleep(0.5)

print('\033[3;35mVALORES SEGUNDA LINHA\033[m')
for valores2 in range(1,4):
    valor = int(input(f'Digite o \033[1;35m{valores2}°\033[m valor da matriz: '))
    if valor %2 ==0:
        valoresPares.append(valor)
    listaSegundaLinha.append(valor)
listaSegundaLinha = [[x] for x in listaSegundaLinha]
print('-' * 40)
sleep(0.5)

print('\033[3;35mVALORES TERCEIRA LINHA\033[m')
sleep(0.5)
for valores3 in range(1,4):
    valor = int(input(f'Digite o \033[1;35m{valores3}°\033[m valor da matriz: '))
    if valor %2 ==0:
        valoresPares.append(valor)
    listaTerceiraLinha.append(valor)
listaTerceiraLinha = [[x] for x in listaTerceiraLinha]
print('-' * 40)
sleep(0.5)

print(listaPrimeiraLinha)
print(listaSegundaLinha)
print(listaTerceiraLinha)
soma = sum(valoresPares)
print('-' * 40)
print(f'Os \033[1mvalores pares da matriz\033[m foram \033[1;35m{valoresPares}\033[m e a soma deles é \033[1;35m{soma}\033[m.')
sleep(1.5)
listaTerceiraColuna = listaPrimeiraLinha[2] + listaSegundaLinha[2] + listaTerceiraLinha[2]
print (f'Os \033[1mvalores da terceira coluna\033[m foram \033[1;35m{(listaPrimeiraLinha[2])}, {(listaSegundaLinha[2])}, {(listaTerceiraLinha[2])}\033[m.')
sleep(1.5)
somaTerceiraColuna = sum(listaTerceiraColuna)
print(f'A \033[1msoma dos valores da terceira coluna\033[m é: \033[1;35m{somaTerceiraColuna}\033[m.')
maiorSegundaLinha = max(listaSegundaLinha)
sleep(1.5)
print(f'Os \033[1mvalores da segunda linha\033[m foram \033[1;35m{listaSegundaLinha}\033[m, e o maior número dessa linha é \033[1;35m{maiorSegundaLinha}\033[m.')