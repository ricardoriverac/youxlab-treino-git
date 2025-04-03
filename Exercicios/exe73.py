#Crie uma tupla preenchida com 20 primeiros colocados da tabela do Campeonato brasileiro de futebol
#Na ordem da colocação. Depois mostre

#Apenas os 5 primeiros colocados
#Os ultimos 4 colocados da tabela
#Uma lista com os times em ordem alfabetica
#Em que posição na tabela esta o time do Flamengo

times = ("Botafogo", "Palmeiras", "Fortaleza", "Internacional", "Flamengo", "São Paulo", "Cruzeiro", "Bahia",
         "Corinthians", "Vitória", "Vasco", "Juventude", "Gremio", "Fluminense", "Atlético - MG", "Bragantino")

print("-=" * 15)
print(f"Os times do brasileirão sao:\n {times}")    
print("-=" * 15)
print(f"Os 5 primeiros times são:\n {times[0:5]}")
print("-=" * 15)
print(f"Os 4 ultimos times são: {times[-4:]}")
print("-=" * 15)
print(f"Os times em ordem alfabetica: {sorted(times)}")
print("-=" * 15)

if "Flamengo" in times:
    print(f"Posição do Flamengo na tabela: {times.index('Flamengo')}")
else:
    print("Flamengo não está na tabela.")

print("-=" * 15)