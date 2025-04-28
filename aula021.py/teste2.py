# def fatorial(num=1):
#     f =1
#     for contador in range(num,0,-1):
#         f *= contador
#     return f  
    
# f1 =fatorial(5)
# f2 =fatorial(4)
# f3 =fatorial(3)

# print(f'Os resultados são {f1} {f2} {f3}')

def par(n=0):
    if n % 2== 0:
        return True
    else:
        return False

num = int(input('Digite um número: '))

if par(num):
    print('É par! ')
    
else:
    print('Não e par! ')  