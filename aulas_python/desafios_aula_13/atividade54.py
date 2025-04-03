import time 
from datetime import datetime

print('\033[1;34m-=-=-=-=-= Grupo da Maioridade =-=-=-=-=-\033[m')
time.sleep(1)

contador = 0
contador2 = 0
for c in range(1, 8):
    ano=int(input('Em que ano a {}ª pessoa nasceu? '.format(c)))
    
    ano_atual = datetime.now().year
    idade = ano_atual- ano
    
    if idade >= 18:
        contador += 1
    else:
        contador2 += 1
        
print('\n=-- Número de pessoas maiores de 18 anos: {} | Número de pessoa menores de 18 anos: {} --='.format(contador, contador2))

print('\033[1;34m-=-=-=-=-= FIM! =-=-=-=-=-\033[m')

    

    