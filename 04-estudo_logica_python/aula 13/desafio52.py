numero= int(input('Descubra se um número é primo:'))
primo = True
total = (numero // 2)

for i in range(total, 0, -1):
    if numero % i == 0 and i != 1:
        primo= False
if primo:
    print("O número {} é primo.".format(numero))
else:
    print("O número {} não é primo.".format(numero))