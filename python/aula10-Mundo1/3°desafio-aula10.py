#par ou impar
numero=int(input('Digite um número:'))
conta= numero % 2
if conta == 0:
    print('Esse número é par!')
else:
    print('Esse número é impar!')