from datetime import date
idade = int (input ("Digite o ano do seu nascimento :  "))
anoatual = date.today().year
data = anoatual - idade
print ("A idade do atleta é: {} anos".format(data))
if data <= 9:
 print ("Você é um atleta MIRIN!!")
elif data <= 14:
 print ("Você é um atleta INFANTIL!!")
elif data <= 19:
 print ("Você é um atleta JUNIOR!!")
elif data <= 20:
 print ("Você é um atleta SÊNIOR!!")
elif data > 20:
 print ("Você é um atleta MASTER!!")

