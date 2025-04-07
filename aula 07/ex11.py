largura = float (input("qual a largura da parede ? "))
altura = float (input ("Qual a altura dessa parede ? "))
area = largura * altura
print ("Sua parede tem a dimensão de {} x {} e sua área é de {}m ".format(largura,altura,area))
tinta = area / 2
print ("Para pintar essa parede você precisara de {}l de tintas ".format(tinta))