valor=float(input('Qual o valor da sua compra?: '))
print('Qual vai ser a forma de pagamento\n'
'1- A vista\n'
'2- Débito\n'
'3- 2x Crédito\n'
'4- 3x ou mais Crédito')
escolha=int(input('Escolha:'))
if escolha==1:
    desconto1=0.1*valor
    print('Você escolheu a opção A VISTA!')
    print(f'Você recebeu um desconto de 10%, valor total:{valor-desconto1}')
elif escolha==2:
    desconto2=0.05*valor
    print('Você escolheu a opção DÉBITO!')
    print(f'Você recebeu um desconto de 5%, valor total:{valor-desconto2}')
elif escolha==3:
    parcela=valor/2
    print('Você escolheu a opção 2x no CRÉDITO!')
    print(f'Valor total é de {valor}, valor da parcela:{parcela}')
elif escolha==4:
    juros=(valor*0.2)
    parcela2=int(input('em quantas vezes você quer parcelar?:' ))
    total=(valor+juros)
    totalParcela=total/parcela2
    print(f'Valor total é de {total} com 20% de juros, valor da parcela:{totalParcela}')



