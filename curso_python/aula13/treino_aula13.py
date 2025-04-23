# Para contar de forma decrescente
for c in range(6, 0, -1):
    print (c)

# Contar de A até B de 2 em 2
for c in range(0, 7, 2):
    print (c)

inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
for c in range(inicio, fim+1, passo):
    print (c)

#Soma os valores
s = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n
print (f'A soma dos valores é {s}. ')