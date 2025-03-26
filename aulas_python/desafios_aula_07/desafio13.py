print('---Calculador de área em METROS---')
a= float ( input('Qual a altura da parede?: '))
l= float ( input('Qual a largura da parede?: '))

s=a*l
r=s/2

print('Pra pintar {} metros quadrados de tinta você vai precisar de {} litros '.format(s, r))