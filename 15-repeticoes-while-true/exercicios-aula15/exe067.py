while True:
    n = int(input('Quer ver tabuada de qual valor: '))
    if n < 0:
        break
    for c in range(0,11):
        print(n , 'X' , c , '=' , c*n )
print('Tabuada encerrada. Volte sempre!')
    
    
