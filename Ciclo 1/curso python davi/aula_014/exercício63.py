n = int (input ('Digite o número: '))
print ()
f1 = c = 1
f2 = f3 = 0
while c < n + 1:
    print (f3, end=' -> ')
    f3 = f1 + f2
    f1 = f2
    f2 = f3
    c += 1
print ('FIM!')