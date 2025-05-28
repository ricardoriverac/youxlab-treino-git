a = float(input('qual o valor da casa ? '))
c = float(input('qual o seu salário? '))
b = float(input('quantos anos você deseja pagar pela casa? '))
d = (a/b) / 12
e = c *0.3
if e >= d:
    print(f'seu empréstimo foi aprovado, a parcela será de {d:.2f}')
else:
    print (f'Seu imprestimo foi recusado o valor da parcela mensal é R${d:.2f} ultrapassou 30% de sua renda mensal R${c}')

