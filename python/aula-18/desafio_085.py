valores = [[], []]  
for c in range(1,8):
    numero= int(input(f'Numero {c}°'))
    valores[numero % 2].append(numero)
print(f'Valores pares digitados: {sorted(valores[0])}')
print(f'Valores impares digitados: {sorted(valores[1])}')