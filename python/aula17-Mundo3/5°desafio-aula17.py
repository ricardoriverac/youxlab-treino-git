#DIVIDINDO VALORES EM LISTAS
pares=[]
impares=[]
numero=[]
while True:
        numero.append(int(input('Digite um número: ')))
        escolha=' '
        while escolha not in 'SN':
                escolha=str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        if escolha=='N':
            break
for indice, valor in enumerate(numero):
    if valor%2==0:
        pares.append(valor)
    if valor%2==1:
        impares.append(valor)
print(f'A lista inteira é: {numero}')
print(f'Os números pares são os {pares}')
print(f'Os números ímpares são os {impares}')