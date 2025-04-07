from datetime import datetime
nascimento= int(input("Em qual ano você nasceu? \n"))
ano_atual = datetime.now().year
idade = (ano_atual - nascimento)
if idade < 18:
    print("Você tem {} anos em {} e vai se alistar daqui a {} anos, em {}.".format(
        idade, ano_atual, (18 - idade), (nascimento + 18)))
elif idade > 18:
    print("Você tem {} anos e já passou seu período de alistamento.".format(idade))
    print("Se não se alistou, deveria ter se alistado em {}, há {} anos atrás.".format(
        (nascimento + 18), idade - 18))
else:
    print("Você tem {} anos. Está na hora de se alistar.".format(idade))