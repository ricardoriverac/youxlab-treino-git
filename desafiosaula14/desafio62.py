from time import sleep
print('{}GERADOR DE PA{} '.format('\033[35m', '\033[m'))
print('-=' * 10)
primeiroTermo = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
print('{}CARREGANDO PA...{} '.format('\033[36m', '\033[m'))
sleep(3)
termo = primeiroTermo
contagem = 1
total = 0
maisTermos = 10
while maisTermos!=0:
    total+=maisTermos
    while contagem <= total:
        print('{} - '.format(termo), end='')
        termo+=razao
        contagem+=1
    print('PAUSA')
    maisTermos = int(input('Quantos termos você quer mostrar a mais?: '))
print('ACABOU')
