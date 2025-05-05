def notas(*num, sit=False):

    cont = maior = menor = media = total = 0

    for c in num:

        cont += 1

        if c > maior:

            maior = c

        if c < menor or cont == 1:

            menor = c

        total += c

    media = total / cont

    if sit:

        print('A situação da turma é: ', end='')

        if media > 7:

            print('Boa!')

        elif media > 5:

            print('Rasoável')

        else:

            print('Ruim!')



    return print(f'A nota total da turma é {total}, maior nota é {maior}, a menor nota é {menor} e a media da turma é {media}')





resp = notas(8, 6, 5, 9, 6, 9, sit=True)

print(resp)
