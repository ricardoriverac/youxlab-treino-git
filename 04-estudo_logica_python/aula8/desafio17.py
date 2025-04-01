import math
co= float(input('comprimento docateto oposto:'))
ca= float (input(' comprimento do cateto adjacente :')) 
hipotenusa= math.hypot(co, ca)
print(' A hipotenusa vai medir {}'.format(hipotenusa))