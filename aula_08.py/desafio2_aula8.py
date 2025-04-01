#co=cateto oposto
#ca=cateto adjacente
import math
co = float(input(' Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hipotenusa = math.hypot(co, ca)
print(' A hipotenusa vai medir {}'.format(hipotenusa))