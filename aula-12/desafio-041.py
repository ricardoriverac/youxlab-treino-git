from datetime import datetime
ano = int(input('Digite o ano de nascimento do atleta:'))
nomeAtleta = str(input('Qual o nome do atleta?'))
ano_atual = datetime.now().year
idade = ano_atual - ano

if idade <=9:
    print('O atleta {} é da categoria MIRIM'.format(nomeAtleta))
elif 9.0 <= idade <= 14:
    print('O atleta {} é da categoria INFANTIL'.format(nomeAtleta))
elif 14.0 <= idade <= 19.0:
    print('O atleta {} é da categoria JUNIOR'.format(nomeAtleta))
elif 19.0 <= idade <= 20.0:
    print('O atleta {} é da categoria SÊNIOR'.format(nomeAtleta))
else:
    print('O atleta {} é da categoria MASTER'.format(nomeAtleta))