import math
num= float(input('Digite qualquer número: '))
parteInt= math.ceil(num)
print('O número {} tem a parte inteira {}'.format(num,math.trunc(parteInt)))