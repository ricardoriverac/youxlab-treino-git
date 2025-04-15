def voto(ano):
  from datetime import date
  atual = date.today().year
  idade = atual - ano
  if idade < 16:
    return f'Com {idade} anos o voto é proibido.'
  elif 16 <= idade < 18 or idade > 65:
    return f'Com {idade} anos o voto é opcional.'
  else:
    return f'Com {idade} anos o voto é obrigatório.'

# Programa principal
nasc = int(input('Ano que vc nasceu: '))
print(voto(nasc))