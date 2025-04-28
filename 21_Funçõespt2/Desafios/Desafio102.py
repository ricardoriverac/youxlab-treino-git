def fatorial(n, show=False):
    f =1 
    for o in  range(n,0 , -1):
        if show:
            print(o,end="")
            if o> 1:
                print(f" x " ,end="")
            else:
                print("=", end="")
        f *= o
    return f    
print(fatorial(5,show= True))