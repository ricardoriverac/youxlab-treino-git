# listnum = []
# um = dois = tres = quatro = cinco = 0
# for c in range(0,2):
#     num = int(input('Digite um valor: '))
#     if num > um:
#         um = num
#         listnum.insert(0,um)
#     elif num > um:
#         dois = num
#         listnum.insert(1,dois)
#     elif num == um:
#         dois = num
#         listnum.insert(1,dois)
#     else:
#         dois = um
#         listnum.insert(1,dois)
#         um = num
#         listnum.insert(0,um)

lista = []

for _ in range(5):

    valor = int(input('Digite um valor: '))
    inserido = False
    
    for i in range(len(lista)):
        if valor < lista[i]:
            lista.insert(i,valor)
            inserido = True
            break
    
    if not inserido:
        lista.append(valor)
print(lista)