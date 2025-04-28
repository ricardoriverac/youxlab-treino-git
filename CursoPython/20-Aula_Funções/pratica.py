def contador(*num):
    print('-=' * 30)
    print(f'Os valores são {num}', end = '')

contador(1, 3, 5, 6, 7)

def dobra(lst):
    pos = 0 
    while pos  < len(lst):
        lst[pos] *=2
        pos+=1
valores=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
dobra(valores)
print(valores)