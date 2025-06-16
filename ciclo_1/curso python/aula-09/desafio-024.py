city = str(input('Fale uma cidade'))
a = city.strip()
b = a.find('santo')

if b == 0:
    print('A sua cidade começa com "santo"')
else:
    print('A sua cidade não começa com "santo"')