peso =float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))
idade = float(input("Digite sua idade "))
imc = peso /(altura**2)
print("{:.2f}".format(imc))
if imc <= 18.5:
    print("Magreza")
elif imc >= 18.5 and imc <= 24.9:
    print("Peso normal")
elif imc >= 25 and imc <= 29.9:
    print("Sobre peso")
elif imc >= 30 and imc <= 34.9:
    print("Obesidade grau 1")
elif imc >= 35 and imc <= 39.9:
    print("Obesidade grau 2")
elif imc >= 40:
    print("Obesidade grau 3")
