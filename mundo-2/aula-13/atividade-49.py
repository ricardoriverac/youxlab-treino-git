num = int(input("Digite um número: "))

print(f"\nTabuada do {num}:")
for i in range(1, 20):
 print(f"{num} x {i} = {num * i}")