print('\033[1;34m-=-=-=-=-= Contando vogais em Tupla =-=-=-=-=-\033[m')

tupla = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')

for p in tupla:
    print(f'\nNa palavra {p.upper()} temos: ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
            
print('\n\033[1;34m-=-=-=-=-= FIM =-=-=-=-=-\033[m')
