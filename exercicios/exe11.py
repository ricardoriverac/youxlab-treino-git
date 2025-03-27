#faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade
#de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m sobre 2.

largura = float(input("Digite a largura da parede em metros: "))
altura = float(input("Digite a altura da parede em metros: "))

area = largura * altura

litrosDeTinta = area / 2

print("A parede tem uma area de {:.2f}m².".format(area))
print("A quantidade de tinta necessária para, pintar a parede e de {:.2f} litros de tinta.".format(litrosDeTinta))      