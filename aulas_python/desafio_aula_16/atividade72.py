lista = ['Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte', 'Vinte e um', 'Vinte e dois', 'Vinte e três', 'Vinte e quatro', 'Vinte e cinco', 'Vinte e seis', 'Vinte e sete', 'Vinte e oito', 'Vinte e nove', 'Trinta', 'Trinta e um', 'Trinta e dois', 'Trinta e três', 'Trinta e quatro', 'Trinta e cinco', 'Trinta e seis', 'Trinta e sete', 'Trinta e oito', 'Trinta e nove', 'Quarenta', 'Quarenta e um', 'Quarenta e dois', 'Quarenta e três', 'Quarenta e quatro', 'Quarenta e cinco', 'Quarenta e seis', 'Quarenta e sete', 'Quarenta e oito', 'Quarenta e nove', 'Cinquenta']

numero = int(input('Digite um número de 0 a 50! '))
if numero > 50:
    numero = int(input('Eu disse de 0 a 50!!!: '))
    
print(f'Você digitou {lista[numero]}')
