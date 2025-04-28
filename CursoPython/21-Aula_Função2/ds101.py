def voto():
    global s
    v=int(input('Em qual ano nasceu? '))
    s = 2025 - v
    return v

print('=' * 20)
voto()
if s >= 18:
    print(f'Sua idade {s}: é obrigatorio')
elif s <= 17:
    print(f'Sua idade {s}:Opcional')
elif s <= 15:
    print(f'Sua idade {s}: Negado')