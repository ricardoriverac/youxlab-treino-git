frase=str(input('Digite uma frase:')).lower().strip()
repeticao=frase.count('a')
primeiroA=frase.find('a')+1
ultimoA=frase.rfind('a')+1
print(f'A letra "A" aparce {repeticao} vezes ')
print(f'A letra "A" aparece a primeira vez no espaço {primeiroA}')
print(f'A letra "A" aparece a ultima vez no espaço {ultimoA}')