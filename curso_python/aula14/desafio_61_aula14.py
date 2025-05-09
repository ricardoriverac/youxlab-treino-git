primeiroTermo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))

termo = primeiroTermo
quantidadeDeTermos = 0

while quantidadeDeTermos < 10:
    print (f'{termo} -> ' , end='')
    termo += razao
    quantidadeDeTermos += 1

print ('FIM')