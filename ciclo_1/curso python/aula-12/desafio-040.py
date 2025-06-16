#crie um programa que leia duas notas de um aluno e calcule sua media mostrando uma menssagem no final de acordo com a media atingida
# - média abaixo de 5.0: REPROVADO!
# - média entre 5.0 e 6.9: RECUPERAÇÃO!
# - média 7.0 ou superior: APROVADO!

nota = float(input('Digite sua nota:'))
nota2 = float(input('Digite dua outra nota:'))
media = (nota + nota2) /2
if media < 5.0:
    print('Você foi REPROVADO!')
elif 5.0 <= media <= 6.9:
    print('Você esta de recuperação!')
else:
    print('Você foi APROVADO!')


#def calcular_media():
    #try:
        #nota1 = float(input("Digite a primeira nota: "))
        #nota2 = float(input("Digite a segunda nota: "))

        #media = (nota1 + nota2) / 2
        #print(f"Média: {media:.1f}")

        #if media < 5.0:
            #print("REPROVADO!")
        #elif 5.0 <= media <= 6.9:
            #print("RECUPERAÇÃO!")
        #else:
            #print("APROVADO!")
    #except ValueError:
        #print("Por favor, insira valores numéricos válidos.")

#calcular_media()
