try:
    a = int(input('Numerador:  '))
    b = int(input('Denominador: '))
    r = a/b 

#except:
#except Exception as erro:
except (ValueError,TypeError):
    #print(f'Infelizmente deu erro {erro.__class__}')
    print('Tivemos problemas ')

except ZeroDivisionError:
    print('Não e possivel dividir por zero ')

except KeyboardInterrupt:
    print('O usuario não infromou dados ')

except Exception as erro:
    print(f'O erro foi: {erro.__cause__} ')

else:

    print(f'O resultado e: {r}')

finally:
    
    print(f'Volte sempre,obrigado')