s1 = float(input('Primeiro segmento: '))
s2 = float(input('Segundo segmento: '))
s3 = float(input('Terceiro segmento: '))
#if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2 :
#s1 != s2 and s1 != s3 or s2 != s1 and s2 != s3 or s3 != s1 and s3 != s2 :
if s1 == s2 and s1 == s3 or s2 == s1 and s2 == s3 or s3 == s1 and s3 == s2 :

    print('Os segmentos podem formar um TRIÂNGULO EQUILATERO')
elif s1 == s2 and s1 != s3 or s2 == s1 and s2 != s3 or s3 == s1 and s3 != s2 :
    print('Os segmentos podem formar um TRIÂNGULO ISÓSCELES')
else:
    print('Os segmentos podem formar um TRIÂNGULO ESCALENO')
