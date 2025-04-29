Extenso = "Zero",'Um',"Dois","Tres","Quatro","Cinco","Seis","Sete","Oito","Nove","Dez","Onze","Doze",'Treze','Quatorze',"Quinze",'Dezeseis',"Dezesete","Dezoito","Dezenove","Vinte"


while True:
    numero = int(input("Digite um numero de 0 a 20: "))
    if numero >= 20:
        print("Erro tente novamente:")
    else:
        break
print(f"Voce digitou o numero {numero} e por extenso fica {Extenso[numero]}")