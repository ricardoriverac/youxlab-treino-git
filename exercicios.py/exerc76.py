from time import sleep
print('-' * 60)
nomeLoja = ('\033[1;36mBEM VINDO A LIVRARIA DA CLARINHA\033[m')
print(nomeLoja.center(60))
sleep(0.8)

lista = ('Corte de espinhos e rosas', 56.80, 'O princípe cruel', 48.20, 'Imperfeitos', 34.70, 'Hipótese do amor', 40.90, 'Estilhaça-me', 45.99, 'Jogos vorazes', 52.10)
print ('-' * 60)
sleep(0.8)
enfeite = ('\033[1mLISTAGEM DE PRODUTOS\033[m')
print(enfeite)
print('-' * 60)
sleep(0.8)

for listagem in range(0, len(lista), 2):
    nomeLivro = lista[listagem]
    preco = lista[listagem+1]
    print (f'{nomeLivro:.<55} R$ {preco:>5.2f}')