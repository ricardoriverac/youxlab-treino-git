PrimeiraNota= float(input("Insira primeira nota "))
SegundaNota = float(input("Insira segunda nota "))
soma = (PrimeiraNota + SegundaNota)
if soma >= 7:
    print("Voce foi aprovado")
elif soma <= 7:
    print("voce ficou de recuperação")
elif soma <= 5:
    print("Voce reprovou")
