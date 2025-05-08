#valores definidos pelo usuário
primeiroTermo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
# armazenar a sequência de números 
sequenciaDeNumeros = ''
termo = primeiroTermo
quantidadeDeTermos = 0
maisTermos = -1

while quantidadeDeTermos < 10:
    sequenciaDeNumeros += str(termo)
    sequenciaDeNumeros += ' -> '
#    print (f'{termo} -> ' , end='')
    termo += razao
    quantidadeDeTermos += 1
print (sequenciaDeNumeros)

while maisTermos != 0:
    maisTermos = int(input('\nDeseja ver mais termos? \nSe sim, digite a quantidade, caso não, digite 0: '))
    if maisTermos == 0:
        print ('FIM DO PROGRAMA')
    else:
        quantidadeDeTermos = 0
        while quantidadeDeTermos < maisTermos:
            sequenciaDeNumeros += str(termo)
            sequenciaDeNumeros += ' -> '
            termo += razao
            quantidadeDeTermos += 1
        print (sequenciaDeNumeros)