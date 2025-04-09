from time import sleep
print('{}GERADOR DE PA{} '.format('\033[35m', '\033[m'))
print('-=' * 10)
primeiroTermo = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
print('CARREGANDO PA... ')
sleep(3)
termo = primeiroTermo
contagem = 1
while contagem <= 10:
    print('{} - '.format(termo), end='')
    termo+=razao
    contagem+=1
print('ACABOU')
    