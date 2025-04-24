import formatar
p = float(input('Digite o valor: '))
print(f'A metade de {formatar.formatar(p)} é {formatar.formatar(formatar.moeda.metade(p))}')
print(f'O dobro de {formatar.formatar(p)} é {formatar.formatar(formatar.moeda.dobro(p))}')
print(f'O valor aumentado deu {formatar.formatar(formatar.moeda.aumentar(p,10))}')
print(f'O valor dimunuido deu {formatar.formatar(formatar.moeda.diminuir(p,13))}')