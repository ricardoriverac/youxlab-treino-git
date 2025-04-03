nome1 = input('Digite seu nome completo: ').strip()
nome2 = nome1.split()
primeiro = nome2[0] 
ultimo = nome2[-1]  
print(f'Primeiro nome: {primeiro}')
print(f'Último nome: {ultimo}')
