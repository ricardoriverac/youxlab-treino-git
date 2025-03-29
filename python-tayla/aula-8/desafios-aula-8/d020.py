import random
primeiro = input('Nome do primeiro aluno: ')
segundo = input('Nome do segundo aluno: ')
terceiro = input('Nome do terceiro aluno: ')
quarto = input('Nome do quarto aluno: ')
lista = (primeiro,segundo,terceiro,quarto)
sorteio = random.choice(lista)
print(f'O aluno escolhido é {sorteio}')