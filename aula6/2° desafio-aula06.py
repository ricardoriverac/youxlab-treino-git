n= input('digite um valor:')
print(n.isnumeric())#se o valor da var. for números é True se não False 
print(n.isalpha())#se o valor da var. for letras é True se não False
print(n.isalnum())#se o valor da var. for letras, números ou os dois juntos é True se não False 
print(n.isupper())#se o valor da var. tem letras maiúsculas é True se não False
print(n.isascii())#se o valor da var. estiverem dentro do conjunto de caracteres ASCII é True se não False
print(n.isdecimal())#se o valor da var. for número decimal é True se não False
print(n.isdigit())#se o valor da var. for um digito é True se não False
print(n.isidentifier())#se o valor da var. tiver todos os caracteres válidos para escrever um identificador no código(ex: letras maiúscula) é True se não False
print(n.islower())#se o valor da var. tem letras minúsculas é True se não False
print(n.isprintable())#se o valor da var. for imprevisível (ex: se var estiver vazia) é True se não False
print(n.isspace())#se o valor da var. tiver espaço é True se não False
print(n.istitle())#se o valor da var. for um título é True se não False
