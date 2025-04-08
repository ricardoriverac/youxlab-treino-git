idade=int (input(' digite a idade do aluno:'))
if idade <= 9 :
    print(' Categoria MIRIM ')
elif idade <= 14 :
    print('Categoria INFANTIL  ')
elif idade <= 19 :
    print('Categoria JUNIOR ')
elif idade <= 20:
    print('Categoria  SÊNIOR ')  
elif idade >  20:
    print('Categoria MASTER ')