casa=float(input('Qual o valor da casa:'))
salario=float(input('Qual é seu salario:'))
anos=float(input('Em quantos anos voce ira pagar a casa?'))
mensal=casa / (anos *12)
porcentagem= salario * 0.3
print ('Para pagar uma casa de R${} em {} anos a prestaçao sera: {}'. format(casa, anos, porcentagem))
if  mensal > porcentagem:
   print('O valor da prestaçao é mais que 30% do seu salario, por isso nao foi aprovado ')
  