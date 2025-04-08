import abjad
acord = abjad.Chord('C4' , 'major')
nota = abjad.Note('C4')
partitura = abjad.Score([acord, nota])
print(partitura)