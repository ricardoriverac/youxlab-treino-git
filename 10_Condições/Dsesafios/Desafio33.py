n1 = int(input("Insira um numero: "))
n2 = int(input("Insira o segundo  numero: "))
n3 = int(input("Insira o terceiro numero  "))
menor = n1
if n2<n1 and n2<n3:
    menor = n2
if n3<n2 and n3<n2:
    menor = n3
maior = n1
if n2>n1 and n2>n3:
    maior = n2
if n3>n2 and n3>n2:
    maior = n3

print("O menor valor e {} ".format(menor))
print("O maior valor e {}".format(maior))