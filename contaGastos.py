from datetime import date
import csv

arquivo_csv = 'gastos.csv'

with open('arquivo_csv', mode="a", newline='', encoding='utf-8') as arquivo:
    escritor = csv.writer(arquivo)


diaAtual = date.today()
gastos = []
somatoria = 0

print(f'Cadastro de gastos do dia: {diaAtual}\n')

while True:
    comQue = input('Para que foi o gasto? ')
    quanto = float(input(f'Quanto foi em {comQue}? R$ '))
    escritor.writerow([diaAtual, comQue, quanto])
    gastos.append((comQue, quanto))
    somatoria += quanto

    continuar = input('Quer continuar? (S/N) ').strip().upper()
    if continuar == 'N':
        break

# Exibindo os gastos organizados
print('\nResumo de gastos:')
print('-' * 30)
for item, valor in gastos:
    print(f'{item:<20} - R$ {valor:.2f}')
print('-' * 30)
print(f'Total gasto no dia {diaAtual}: R$ {somatoria:.2f}')
print('Gastos registrados com sucesso!')


# from datetime import date
# diaAtual = date.today()
# gastosTotal = []
# somatoria = []
# comQue = str(input(f'Para onde foram os gastos de hoje? {diaAtual} ? '))
# gastosTotal.append(comQue)
# quanto = float(input(f'Quanto foi em {comQue}? '))
# gastosTotal.append(quanto)
# somatoria.append(quanto)
# continuar = str(input('Quer continuar? (S/N) ')).upper()
# if continuar == 'S':
#     while True:
#         comQue = str(input(f'Ok, Para qual foi o próximo gasto no dia {diaAtual} ? '))
#         gastosTotal.append(comQue)
#         quanto = float(input(f'Quanto foi {comQue}? '))
#         gastosTotal.append(quanto)
#         somatoria.append(quanto)
#         continuar = str(input('Quer continuar? (S/N) ')).upper()
#         if continuar == 'N':
#             for movimento in gastosTotal:
#                 print(movimento)
#                 print(f'Valor gasto: R${quanto:.2f}')
#                 print('----------------')
#             print(f'seu gasto total no dia ({diaAtual}) foi de R${sum(somatoria)}')
#             break

    

