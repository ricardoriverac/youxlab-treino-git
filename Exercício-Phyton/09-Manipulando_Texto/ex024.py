nome = str(input('Cidade: '))

palavra = ('Santo')

posicao =nome.find(palavra)

if posicao != -1:
    
    print('A palavra {}, foi encontrada na posição {} do texto'.format(palavra, posicao))
