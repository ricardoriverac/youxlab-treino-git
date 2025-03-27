frase = str(input('Digite algo: ')).upper().strip()
fa = frase.count('A')
fp = frase.find('A')+1
fu = frase.rfind('A') 
print(f'A letra A aparece {fa} vezes na frase')
print(f'A primeira posição do A fica na posição {fp}')
print(f'A ultima posição do A fica na posição {fu}')