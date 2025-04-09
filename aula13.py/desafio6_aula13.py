primeiro = int(input('Qual o primeiro termo:'))
razao = int(input('Qual é a razão da PA:'))
dec = primeiro + (10 - 1) * razao 
for c in range(primeiro, dec, razao):
    print("{}".format(c), end=",")
print('Fimmm')