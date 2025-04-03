nota1 = int (input ("Digite a primeira nota do aluno: "))
nota2 = int (input ("Digite a segunda nota do aluno: "))
media = (nota1 + nota2) / 2 
print ("PRIMEIRA nota \033[36m{}\033[m SEGUNDA nota \033[36m{}\033[m  a MÉDIA é: \033[36m{}\033[m ".format(nota1,nota2,media))
if media < 5:
    print ("Média abaixo de 5, \033[31mREPROVADOO")
elif media > 5 or media < 6.9:
      print ("Média entre 5.0 e 6.9, \033[33mRECUPERAÇÃO")
elif media >= 7:
      print ("Média acima de 7, \033[32mAPROVADO")