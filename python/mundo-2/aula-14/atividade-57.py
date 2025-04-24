sexo = input("Informe seu sexo [M/F]: ").strip().upper()

while sexo not in ['M', 'F']:
    print("Entrada inválida. Por favor, digite apenas 'M' para masculino ou 'F' para feminino.")
    sexo = input("Informe seu sexo [M/F]: ").strip().upper()

print(f"Sexo '{sexo}' registrado com sucesso!")
