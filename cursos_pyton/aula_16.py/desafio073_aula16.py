times = (
    "Botafogo", "Palmeiras", "Flamengo", "Fortaleza", "Internacional",
    "São Paulo", "Corinthians", "Bahia", "Cruzeiro", "Vasco da Gama",
    "Vitória", "Atlético-MG", "Fluminense", "Grêmio", "Juventude",
    "Red Bull Bragantino", "Athletico-PR", "Criciúma", "Atlético-GO", "Cuiabá"
)

print()
print(f"a) Primeiros 5 colocados do Brasileirão: \n{times[0:5]}")
print()
print(f"b) Últimos 4 colocados: \n{times[-4:]}")
print()
print("c) Times em ordem alfabética:\n")
for time in sorted(times):
    print(time)
print()
# Posição do Juventude (corrigido)
juvent = times.index("Juventude") + 1
print(f"d) O Juventude está na {juvent}ª posição.")
