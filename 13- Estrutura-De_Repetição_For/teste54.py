contador = 0
contador2 = 0
for c in range(1, 8):
    ano = int(input('digite sua data de nascimento: '))
    cou = 2025 - ano
    if cou >= 18:    
        n1 = cou - cou + 1    
        contador += n1    
    elif cou <= 18:
        n2 = cou - cou + 1 
        contador2 += n2 
print('{} JÁ SAO MAIORES DE IDADE'.format(contador))
print('{} AINDA SAO MENORES!'.format(contador2))
    




   