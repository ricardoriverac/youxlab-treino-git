mum = (int(input('Digite um numero: ')),
       int(input("Digite outro numero: ")),
       int(input("Digite mais um numero: ")),
       int(input("Digite o ultimo numero " )))
print(f"Voce digitou os valores{mum}")
print(f"O valor 9 apareceu {mum.count(9)} vezes")
print(f"O valor 3 apareceu na {mum.index(3)+1} posiçao")
print("os valores pares digitaram foram ", end="")
for n in mum :
    if n  % 2 == 0:
        print(n,end=" ")