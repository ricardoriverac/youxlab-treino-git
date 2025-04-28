for c in range(0, 6):
   print(c)
print('FIM')

#contar pra tras
for c in range(6, 0, -1):
   print(c)
print('FIM')

#contar de 2 em 2
for c in range(0, 9, 2):
   print(c)
print('FIM')

#contar até o número escolhido
n = int(input('Digite um número: '))
for c in range(0, n+1):
   print(c)
print('FIM')

#mesma coisa do de cima so q com mais detalhes
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
print('FIM')

#repetindo frases
for c in range(0, 3):
    n = int(input('Digite um valor: '))
print('FIM')

#fazendo somatoria
s = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n
print(f'A somatória de todos os valores é {s}')