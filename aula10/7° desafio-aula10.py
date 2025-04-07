#Aumento salarial
salario=float(input('Qual o seu sálario?: '))
if salario>1250.00:
    aumento1= salario*1.10
    print('Seu aumento foi de 10%, então seu sálario é:{:.2f}'.format(aumento1))
if salario<1250.00:
    aumento2= salario*1.15
    print('Seu aumento foi de 15%, então seu sálario é:{:.2f}'.format(aumento2))