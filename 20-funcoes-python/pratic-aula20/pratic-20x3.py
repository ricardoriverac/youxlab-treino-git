def dobro(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


#programa principal
valores = [7,2,3,5,8,1]
print(valores)
print(f'Os valores {valores} dividos foram {dobro(valores)}')

