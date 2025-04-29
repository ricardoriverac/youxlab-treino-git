produto= ''
preco= 0
count= 0
produtos= 0
total= 0
usuario= ''
print('CONSULTOR DE PRODUTOS')
print('='*22) 
while True:
    produto=input('Digite o nome do produto: ')
    preco= float(input('Digite o preço desse produto: R$'))
    count +=1
    total= produto
    print(total)
    if preco == 1000:
        produto= preco
        count += 1
        print(f'{count} produto(s) custa(m) mais de R$1000.')
    usuario=input('Deseja continuar?: ').upper() .capitalize()
    if usuario == 'N':
        break
