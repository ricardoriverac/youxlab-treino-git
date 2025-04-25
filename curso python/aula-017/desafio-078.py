lista = []
maior = 0
menor = 999999
for i in range(5):
    num = int(input('Digite umm valor: '))
    lista.append(num)
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    p = lista.index(num)
    
    print(f'O {num} está na posição {p}')
print(f'O  maior número foi o {maior}')
print(f'O menor número foi o {menor}')
