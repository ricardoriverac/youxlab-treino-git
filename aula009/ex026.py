nom = str(input('M ediga um nome ')).upper().strip()
print('No nome temos ao todo {} letras a '.format(nom.count('a')))
print ('A letra esolhida foi mostrada pela primeira vez na posição:{} '.format(nom.find('A')+1))
print ('A letra esolhida foi mostrada pela ultima  vez na posição:{} '.format(nom.rfind('A')+1))
