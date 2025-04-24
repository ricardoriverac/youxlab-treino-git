print('Descubra se suas retas formam um triangolo: ')

reta1 = float(input('Quantos cm tem a primeira reta? '))
reta2 = float(input('Quantos cm tem a segunda reta? '))
reta3 = float(input('quantos cm tem a segunda reta? '))

if reta3 + reta2 >= reta1 and reta1 + reta2 >= reta3 and reta1 + reta3 >= reta2:
    print('Pode-se formar um triângulo')
else:
    print('Não pode-se formar um triângulo')