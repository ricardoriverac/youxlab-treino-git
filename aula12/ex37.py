numero = int (input ("Digite um número : "))
print (" Digite uma das bases para conversão:  ")
print ("[1] Converter para binário. ")
print ("[2] Converter para octal. ") 
print ("[3] converter para hexadecimal.")
opcao = int (input ("Digite sua opção: "))
if opcao == 1:
    print ("O número digitado {} convertido para BINÁRIO {}".format(numero,bin(numero)[2:]))
elif opcao == 2:
    print ("O número digitado {} convertido OCTAL {}".format(numero,oct(numero)[2:]))
elif opcao == 3:
    print ("O número digitado {} convertido para HEXADECIMAL {}".format(numero,hex(numero)[2:]))
else:
    print ("Comando não encontrado, digite novamente! ")