from math import hypot
catetoOposto = float (input ("Digite o valor do cateto oposto : "))
catetoAdjacente = float (input ("Agora o valor do cateto adjacente : "))
hipotenusa = hypot(catetoOposto, catetoAdjacente)
print ("a Hipotenusa vai medir {:.2f} !!".format(hipotenusa))