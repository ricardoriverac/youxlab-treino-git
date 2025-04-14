print("============"*2)
print(" SEQUENCIA DE FIBONACCI")
print("============"*2)
print()
n = int(input("Digite um numero: "))
f1 =c =1
f2 = f3=0
while c< n +1:
    print( f3,end=" -> ")
    f3 = f1 + f2
    f1 = f2
    f2 = f3
    c += 1
    print("FIM")
