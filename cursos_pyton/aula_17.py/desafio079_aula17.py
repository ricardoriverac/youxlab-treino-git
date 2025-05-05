lista = []
while True:
    entrada = (int(input('Digite um valor: ')))
    if entrada not in lista:
        lista.append(entrada)
        print('\033[32mO número foi adicionado com sucesso')
        print()
    else:
        print('\033[38;5;208mo número já se encontra na lista')
    pergunta = ' '
    print()
    while pergunta not in 'NS':
        pergunta = str(input('Deseja continuar? [S/N] ')).upper()
    if pergunta in 'N':
        break
    print()
print(f'Você digitou os valores {sorted(lista)}.')
