#testando as condições aninhadas:
nome= str(input('Digite seu nome: '))
if nome == 'Alice':
    print('Que nome lindo!')
elif nome == 'Maria' or nome== 'Lucas' or nome== 'Gabriel' or nome== 'Ana':
    print('Seu nome é bem comum e popular no Brasil!')
elif nome in 'Olívia Juliana Antonela':
    print('Belíssimo nome!')
else:
    print('Tenha um bom dia, {}!'.format(nome))