casa = float(input('\033[1mValor da casa: '))
sal = float(input('Salário do comprador: '))
ano = int(input('Quantos anos de financiamento:\033[m '))
porc = sal * 0.30
fin = ano * 12
pres = casa / fin
print(f'Para pagar uma casa de R${casa} em {ano} anos a prestação será de {pres: .2f} ')
if porc < pres:
    print('\033[1;31mEMPRÉSTIMO NEGADO!')
else:
    print('\033[1:32mEMPRÉSTIMO ACEITO!')