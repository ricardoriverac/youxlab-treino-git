#Adicionando cores no python
#Exemplo "\033[0;30;40m"
# \033 = Comando para colar cores. 
# "0 = o estilo da letra" 
# "30 = a cor dos textos "
# "40 = a cor das letras "
# DICA: sempre digite "m" primeiro antes de abrir um []
print('\033[30;40mBranco\033[m')
print('\033[31;41mVermelho\033[m')
print('\033[32;42mVerde\033[m')
print('\033[33;43mAmarelo\033[m')
print('\033[34;44mAzul\033[m')
print('\033[35;45mRoxo\033[m')
print('\033[36;46mCiano\033[m')
print('\033[37;47mCinza\033[m')
print('_'*10)
#Exemplos de estilos de letras
print('\033[0mNada\033[m')
print('-'*10)
print('\033[1mGrifa\033[m')
print('-'*10)
print('\033[4mUnderline\033[m')
print('-'*10)
print('\033[7mNegativo\033[m')