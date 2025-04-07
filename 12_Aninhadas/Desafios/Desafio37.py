n1 = int(input("Insira um numero inteiro: "))
n2 = str(input("Digite 1 para binário 2 para octal 3 para hexadecimal: "))

if n2 == "1":
    print("Numero convertido para binario{}, ".format(print(bin(n1))))

elif n2 == "2":

    print("Numero convertido octal{},".format(print(oct(n1))))

elif n2 == "3":

    print("Numero convertido para hexadecimal{}".format(print(hex(n1))))