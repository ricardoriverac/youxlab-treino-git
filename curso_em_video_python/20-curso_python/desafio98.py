from time import sleep

frase = ('\033[1;36mCONTAGEM DE 1 A 10\033[m') 
frase2 = ('\033[1;36mCONTAGEM DE 10 A 0 PULANDO DE 2 EM 2\033[m ')
frase3 = ('\033[1;36mAGORA SUA VEZ!\033[m')

print('~' *len(frase))
sleep(0.2)
print(f'{frase}')
sleep(0.2)
print('~' *len(frase))
sleep (1)

for contagem in range(1, 11):
    print(f'{contagem}', end = '  ', flush=True)
    sleep(0.2)
print('\n')

print('~' *len(frase2))
sleep(0.2)
print(f'{frase2}')
sleep(0.2)
print('~' *len(frase2))
sleep (1)

for contagem2 in range(10, 0, -2):
    print(f'{contagem2}', end ='  ', flush=True)
    sleep(0.2)
print('\n')
    
print('~' *len(frase3))
sleep(0.2)
print(f'{frase3}')
sleep(0.2)
print('~' *len(frase3))
sleep (1)

inicio = int(input('\033[1mDigite o número que deseja começar:\033[m '))
fim = int(input('\033[1mDigite o número final:\033[m '))
passo = int(input('\033[1mDe quanto em quanto deseja pular?\033[m '))

def contador(i, f, p):
    for cont in range(i, f, p):
        print(f'{cont}', end=' ', flush=True)
        sleep(0.2)
    print('\n')
    if f<i:
        for cont in range(i, f, -p):
            print(f'{cont}', end=' ', flush=True)
            sleep(0.2)
    print('\n')
contador(inicio, fim, passo)