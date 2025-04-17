def fatorial(n):
    f = 1
    for c in range(1,n+1):
        f *= c
    return f 


num=int(input('Digite: '))
fat=fatorial(num)
print(f'O fatorial do número {num} é {fat}')