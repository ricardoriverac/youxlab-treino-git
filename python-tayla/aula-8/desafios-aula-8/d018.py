import math
oposto = float(input('Digite o valor do cateto oposto: '))
adjacente = float(input('E o valor do cateto adjacente: '))
hipotenusa = math.hypot(adjacente,oposto)
print(f'O valor da hipotenusa é {hipotenusa}')