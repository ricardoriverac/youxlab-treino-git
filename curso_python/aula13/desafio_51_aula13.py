primeiroTermo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
pA = primeiroTermo + (11 - 1) * razao
print ('Os dez primeiros termos desta PA são: ')
for computador in range(primeiroTermo, pA, razao):
    print (f'{computador} -> ' , end=' ')