def fatorial(num, show=False):
    f = 1
    for i in range(num, 0, -1):
        f *= i
        if show:
            print(i, end=' x ' if i > 1 else ' = ')
    return f
print(fatorial(5))
print(fatorial(5, show=True))
