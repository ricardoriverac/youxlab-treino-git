imo = float(input('Qual o valor do imóvel? '))
sal = float(input('Quanto é o seu salário? '))
anos = float(input('Em quantos anos você quer parcelar? '))
numpar = anos*12
par = imo / numpar
if par == 0.3 * sal:
    print('Você pode prosseguir com o financiamento do imóvel!')
elif par > 0.3 * sal:
    print('Você, infelizmente, não pode fazer o financiamento...')
else:
    print('Parabéns! Você foi aprovado para o financiamento!')
