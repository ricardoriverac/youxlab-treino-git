nome = str (input ("Digite seu nome: "))
if nome == "gustavo":
    print ("Que nome bonito!")
elif nome == "maria" or nome == "pedro" or nome == "Paulo":
    print ("Seu nome é bem popular no Brasil! ")
else:
    print ("Seu nome é normal!")
print ("Tenha um bom dia, {}!".format(nome))