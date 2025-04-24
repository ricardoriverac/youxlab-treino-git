import math

angulo = float(input("Digite um ângulo em graus: "))
radiano = math.radians(angulo)
seno = math.sin(radiano)
cosseno = math.cos(radiano)
tangente = math.tan(radiano)

print(f"Seno de {angulo}°: {seno:.4f}")
print(f"Cosseno de {angulo}°: {cosseno:.4f}")
print(f"Tangente de {angulo}°: {tangente:.4f}")
