maiorpeso = 0
menorpeso = 0
for c in range(1,6):
    peso = float(input(f'Digite o peso da {c}° pessoa: '))
    if c == 1 :
        maiorpeso = peso
        menorpeso = peso
    else:
        if peso > maiorpeso:
            maiorpeso = peso
        if peso < menorpeso :
            menorpeso = peso 
print(f'O maior peso foi {maiorpeso}')
print(f'O menor peso foi {menorpeso}')
