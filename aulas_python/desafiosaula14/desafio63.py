print('{}SEQUÊNCIA DE FIBONACCI{}'.format('\033[35m', '\033[m'))
numero = int(input('Quantos termos você quer mostrar?: '))
total = numero
termo1 = contagem = 0
termo2 = termo3 = 1
while contagem < numero +1:
    print(termo1, end=' → ')
    termo3 = termo1+termo2
    termo1 = termo2   
    termo2 = termo3
    contagem+=1
print('ACABOU')

