sl = float(input('Qual é o salário de um funcionário? R$'))
if sl >= 1250.00 :
    aum = sl + (sl * 10/100)
else:
    aum = sl + (sl * 15/100)
print(f'Quem ganhava R${sl} passar a ganhar R${aum:.2f} agora')