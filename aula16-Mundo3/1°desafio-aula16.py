#NÚMEROS POR EXTENSO
numeros=("zero","um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez","onze",
        "doze","treze", "quatorze", "quinze","dezesseis", "dezessete", "dezoito", "dezenove", "vinte")
escolha=int(input('Digite um n° de 1 à 20 para ser escrito por extenso:'))
while escolha<0 or escolha>20:
    escolha=int(input('ERRO, digite um n° de 1 à 20 para ser escrito por extenso:'))
print(f'Este n° por extenso é: {numeros[escolha]}')