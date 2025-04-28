from random import shuffle
primeiro = input('Primeiro aluno: ')
segundo = input('Segundo aluno: ')
terceiro = input('Terceiro aluno: ')
quarto = input('Quarto aluno: ')
lista = [primeiro,segundo,terceiro,quarto]
shuffle(lista)
print('A ordem da apresentação será ')
print(lista)