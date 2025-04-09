numero= int(input('Digite o primeiro termo da P.A. : '))

razao = int(input('Digite a razão da P.A. : '))

termo = numero + (9) * razao 

for i in range(numero,termo + razao, razao):
    formula = numero + razao

    print(i, end=' --> ')