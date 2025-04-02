numero=int(input('Digite um numero:'))
unidade=numero // 1 % 10
dezena= numero // 10 % 10
centena= numero // 100 % 10
milar=numero // 1000 % 10
print('Analisando o numeo:{}'. format(numero))
print('Sua unidade é:{}'. format(unidade))
print(' Sua dezena é:{}'. format(dezena))
print('Sua centena é:{}'. format(centena))
print('seu milar é:{}'. format(milar))