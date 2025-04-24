c = ('\033[1m\033[m',   # 0 sem cores
     '\033[1;30;41m',   # 1 - vermelho
     '\033[1;30;42m',   # 2 - verde
     '\033[1;30;43m',   # 3 - amarelo
     '\033[1;30;44m',   # 4 - azul
     '\033[1;30;45m',   # 5 - roxo
     '\033[1;30;46m',   # 6 - ciano
     '\033[1;30;47m',   # 7 - cinza
     '\033[7;30m'      # 8 - branco  
);
  

def titulo(msg,cor=0): 
  tam = len(msg) + 4
  print(c[cor], end='')
  print('=' * tam)
  print(f'  {msg}   ')
  print('=' * tam)
  print(c[0])


def ajuda(v):
  titulo(f'ACESSANDO O MANUAL DO \' {v} \'', 4)
  print(c[8], end=' ')
  help(v)
  print(c[0], end='')


#programa principal
while True:
  titulo('SISTEMA PYHELP', 2)
  n = input('Funções ou bibliotecas: ', )
  if n.upper() == 'FIM':
    break
  else:
    ajuda(n)
titulo('ATÉ LOGO',1)
