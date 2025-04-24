from random import randint
numerosdeTentativas = 1
computador = randint(0,10)
print("""Computador ta pensando em número entre 0 a 10 
\033[36mTente adivinhar\033[m""")
jogador = int(input('Digite o número: '))
while jogador != computador :
    jogador = int(input('\033[31mErrou!.\033[m Tente novamente: '))
    if jogador > computador :
        print('Menos... Tente mais uma vez.')
    else:
        print('Mais... Tente mais uma vez.')
    numerosdeTentativas += 1
print(f'O número de tentativas até acertar foi {numerosdeTentativas}')
    

