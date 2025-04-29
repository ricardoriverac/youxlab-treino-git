# nome = str(input("Qual e seu nome? ")).strip()
# if nome == "Victor":
#     print("ola {} que nome legal".format(nome))
# else:
#     print("Ola {}, que nome estranho!".format(nome))
# print("Bom dia")
n1 = float(input("Primeira nota do aluno: "))
n2 = float(input("Segunda nota do aluno: "))
m = (n1 + n2)/2
print("Sua media e {:.1f}".format(m))
if m >= 6:
    print("Voce foi aprovado")
else:
    print("Voce reprovou:")

