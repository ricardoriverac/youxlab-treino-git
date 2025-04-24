import re
palavras = ('aprender', 'programar', 'linguagem', 'python',
            'curso', 'gratis', 'estudar', 'praticar', 'trabalhar',
            'mercado', 'programador', 'futuro')
for i in range(0, len(palavras)):
    print(f'Na palavra {palavras[i].upper()} temos as vogais: {re.findall(r"[aeiou]", palavras[i])}')
