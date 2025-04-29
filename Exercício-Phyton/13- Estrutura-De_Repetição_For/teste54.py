contador = 0
contador2 = 0
for c in range(1, 8):
    ano = int(input('digite sua data de nascimento: '))
    c = 2025 - ano
    if c >= 18:    
        priumero = c - c + 1    
        contador += priumero 
    elif c <= 18:
        segnNumero = c - c + 1 
        contador2 += segnNumero
print('{} JÁ SAO MAIORES DE IDADE'.format(contador))
print('{} AINDA SAO MENORES!'.format(contador2))
    




   