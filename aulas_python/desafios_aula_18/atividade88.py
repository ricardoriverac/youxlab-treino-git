import random
import time 

Números = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 
'11', '12', '13', '14', '15', '16', '17', '18', '19', '20', 
'21', '22', '23', '24', '25', '26', '27', '28', '29', '30', 
'31', '32', '33', '34', '35', '36', '37', '38', '39', '40', 
'41', '42', '43', '44', '45', '46', '47', '48', '49', '50', 
'51', '52', '53', '54', '55', '56', '57', '58', '59', '60']

print('-'*30,'\n        JOGA NA MEGA SENA\n','-'*30)

Quantidade = int(input('Quantos jogos você quer que eu sorteie?: '))

print(f'-=-=-= Sorteando {Quantidade} JOGOS =-=-=-')
print('Carregando...')
time.sleep(2)

for c in range (Quantidade):
    print(f'{c+1}° JOGO: {random.sample(sorted(Números), 6)} ')
    time.sleep(1)

print('-=-=-=-=-= < BOA SORTE! > =-=-=-=-')