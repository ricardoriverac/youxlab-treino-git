#num.insert(2, 2) vai inserir o na posição 2 o número 2 Comando insert insere um item especifico na lista
#len(lista)
#num.remove(2) vai remover o o elemento 2 da lista

#num.pop() remove o valor num.pop(2) vai remover o elemento 2 d lista

lista = []
while True:
    nome = int(input('Valor: '))
    lista.append(nome)
    print(lista)
    if lista.insert(10):
        break
