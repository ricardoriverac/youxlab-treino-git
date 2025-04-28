sx = str(input('qual o seu sexo: [M/F]          '  .strip().upper())) [0]
while sx not in 'MFmf':
    sx  = str(input('gênero errado. por favor, tente novamente. ')).strip().upper() [0]