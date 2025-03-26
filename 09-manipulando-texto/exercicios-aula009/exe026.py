frase = str(input('Digite algo: ')).upper().strip()
fp = frase.find('A')+1
fu = frase.rfind('A') 
print(frase.count('A'))
print(f'A primeira posição do A fica na posição {fp}')
print(f'A ultima posição do A fica na posição {fu}')