#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua média

nome = str(input("Qual é o seu nome? "))
nota = float(input("Qual é a primeira nota? "))
nota2 = float(input("Qual é a segunda nota? "))
media = (nota + nota2) / 2

print("Sua média de {} é {} é de {}.".format(nota, nota2, media))

if media >= 6:
    print("Aluno Aprovado")
elif media >= 4:
    print("Aluno em recuperação")
else: print("Aluno reprovado")