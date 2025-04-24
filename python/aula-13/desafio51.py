primeiro = float (input('Primeiro Termo: '))
razao = float (input('Razão: '))

t = primeiro
for c in range (1, 11):
    print ('{:.2f}'.format(t))
    t = t + razao