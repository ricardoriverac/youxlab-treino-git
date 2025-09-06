num = int(input("diga um número: "))
ct = 0
for i in range(1, num + 1):

    if num % i == 0:
        ct += 1
print("o número {} foi divisível {} vezes!".format(num, ct))
if ct == 2:
    print("o número é primo")
else:
    print("O número não é primo")