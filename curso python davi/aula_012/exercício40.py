nt1 = float(input('primeira nota ' ))
nt2 = float(input('segunda nota ' ))
média = (nt1 + nt2) / 2
print ('somando a nota {:.1f} e a nota {:.1f} a média do aluno é {:.1f}'.format(nt1, nt2, média))
if média > 7 :
    print(' aprovado.')
elif média < 5:
    print('reprovado.')
else:
    média > 5 < 7
    print('recuperação')