pessoa = {
    'nome': 'Gustavo',
    'idade': 69,
    'sexo': 'm'    
}


carro = {
    'marca': 'chevrolet',
    'anoFabricacao': 2020,
    'anoModelo': 2021,
    'dono': 'gustavo',
    'carro': 'jetta'
}
pessoa['peso'] = 98.8
for k , v in pessoa.items():
    print(k , v)