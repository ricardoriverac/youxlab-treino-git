
valores = []
quantidade = int(input("Quantos números você quer digitar? "))
for i in range(quantidade):
    numero = int(input(f"Digite o {i+1}º número: "))
    valores.append(numero)
    valores.sort()
    
print(f"Os números digitados foram: {valores}", )
if 5 in valores:
    print('Tem um valor 5')
else:
    print('Não tem um valor 5')
print(f'A quantidade de valores digitados foi {len(valores)}')
