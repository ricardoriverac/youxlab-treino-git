p = float(input('Preço do produto , sem o desconto: '))
pr = int(input('Digite o desconto em porcentagem que você quer dar pro cliente: '))
nv = p - (p * pr/100) 
print(f'O preço do produto com um desconto de {pr}% é? R${nv:.2f}')