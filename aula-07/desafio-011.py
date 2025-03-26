a = float(input('Qual a altura da sua parede?'))
l = float(input('Qual a Largura?'))
r = l * a
t = r /2
print ('sua parede tem a dimensão de {} x {} e sua area é de {:.2f}m2 \n  logo para pintar sua parede necessario {:.2f}L '.format(l, a, r, t))
