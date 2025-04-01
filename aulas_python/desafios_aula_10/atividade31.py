print('---Bem vindo(a) a nossa impressa de viagens!---')
km = float(input('Qual a distancia da sua viagem? Acima de 200km terá um desconto! '))

if km <= 200:
    q = km*0.50
    print('O preço é: R${:.2f}'.format(q))
    
else:
    w = km*0.45
    print('O preço com nosso desconto é: R${:.2f}'.format(w))