primter = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Qual a razão da PA: '))

for t in range(primter, primter*11, razao):
    print(t,end=' ')
print('. Ai está os termos que você pediu')