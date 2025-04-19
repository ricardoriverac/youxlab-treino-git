from time import sleep
print('\033[1;35mVAMOS FAZER UMA MATRIZ\033[m')
sleep(1)
listaPrimeiraLinha = list()
listaSegundaLinha = list()
listaTerceiraLinha = list()

print ()

print('\033[3;35mVALORES PRIMEIRA LINHA\033[m')
for valores1 in range(1,4):
    valor = int(input(f'Digite o \033[1;35m{valores1}°\033[m valor da matriz: '))
    listaPrimeiraLinha.append(valor)
listaPrimeiraLinha = [[x] for x in listaPrimeiraLinha]
print('-' * 40)
sleep(1)

print('\033[3;35mVALORES SEGUNDA LINHA\033[m')
for valores2 in range(1,4):
    valor = int(input(f'Digite o \033[1;35m{valores2}°\033[m valor da matriz: '))
    listaSegundaLinha.append(valor)
listaSegundaLinha = [[x] for x in listaSegundaLinha]
print('-' * 40)
sleep(1)

print('\033[3;35mVALORES TERCEIRA LINHA\033[m')
for valores3 in range(1,4):
    valor = int(input(f'Digite o \033[1;35m{valores3}°\033[m valor da matriz: '))
    listaTerceiraLinha.append(valor)
listaTerceiraLinha = [[x] for x in listaTerceiraLinha]
print('-' * 40)
sleep(1)

print(listaPrimeiraLinha)
print(listaSegundaLinha)
print(listaTerceiraLinha)