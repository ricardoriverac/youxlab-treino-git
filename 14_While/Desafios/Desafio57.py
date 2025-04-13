sexo = str(input("Informe seu sexo [M/F]: ")).upper()[0] .strip()
while sexo not in "MF":
    sexo = str(input("Invalido!, Tente novamente, Informe seu sexo: ")).strip().upper()[0]
print(f"Seu sexo e {sexo}, foi registrado com sucesso")
