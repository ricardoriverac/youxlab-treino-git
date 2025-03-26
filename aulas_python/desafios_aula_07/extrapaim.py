print('---Descontarei a especifica % do valor que colocar aqui---')
v= float ( input('Qual o valor? (Sem desconto) '))
p= float (input('Qual a porcentagem? (Para ser descontada) '))

e=p/100*v
r=v-p
print('O resultado é R$',r)