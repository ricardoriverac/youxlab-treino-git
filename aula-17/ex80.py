lista = []
for i in range(5):
    num = int(input(f'Digite um número para a posição {i + 1}ª: '))
    posicao_inserir = 0 
    while posicao_inserir < lista.count('(' , ')') and lista[posicao_inserir] < num:
        posicao_inserir += 1
    lista.insert(posicao_inserir, num)
print(lista)