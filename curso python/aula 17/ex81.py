continuacao = 'S'
lista = []
while continuacao == "S":
    numero = int (input ("Digite um número \033[34m\033[m : "))
    lista.append(numero)
    continuacao = str (input ("Quer continuar [S/N] ? ")).strip().upper()
    lista.sort(reverse = True)
print ("\tForam digitados", len(lista), "números!")
print (f"\tA lista ordenada de forma decrescente {lista}")
if 5 in lista:
    print (f"\tO número 5 foi digitados , {lista.count(5)} x.")
else:
    print("\tNão foi digitado o valor 5.")
