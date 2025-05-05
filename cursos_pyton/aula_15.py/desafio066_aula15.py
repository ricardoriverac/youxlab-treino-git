c = s = 0
while True:
    n = int(input('Digite um número: ( Digite 999 para parar): '))
    if n == 999:
        break
    c += 1
    s += n
print(f'Foram digitados ao todo {c} números e a soma entre eles é {s}')