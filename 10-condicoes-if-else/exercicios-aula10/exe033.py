a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
menor = a
if b < a and b < c :
    menor = b
if c < a and c < b :
    menor = c
#Verificando com números valores maiores
maior = a
if b > a and b > c :
    maior = b
if c > a and c > b :
    maior = c
print(f'O maior valor foi o {maior}')
print(f'O menor valor foi o {menor}')     
      