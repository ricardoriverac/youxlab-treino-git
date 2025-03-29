import random
primeiro = input('Nome do primeiro aluno(a): ')
segundo = input('Nome do segundo aluno(a): ')
terceiro = input('Nome do terceiro aluno(a): ')
quarto = input('Nome do quarto aluno(a): ')
lista = (primeiro,segundo,terceiro,quarto)
sorteio = random.choice(lista)
print(f'O aluno escolhido é {sorteio}')