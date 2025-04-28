expressao = input('Digite uma expressão: ')
pilha = []

for simb in expressao:
    if simb == '(': # Cada vez que o parêntese abrir pega um parêntese aberto e joga na pilha
        pilha.append('(')  
    elif simb == ')': # Ou a lista tá vazia ou cheia
        if len(pilha) > 0: # Não está vazio
            pilha.pop()    
        else: # Se a pilha estiver vazia
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está \033[36mCORRETA!\033[m ')
else:
    print('Sua expressão está \033[31mERRADA!\033[m ')

