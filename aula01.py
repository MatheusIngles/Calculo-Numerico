# Ipython

from math import pi

def soma(a,b):
    return a + b

def operacoes(a,b):
    return a+b, a*b

def inst(a,b,c=2):
    return a+b*c

def volume(raio):
    return 4/3 * pi * (raio**3) 

if __name__ == "__main__": 
    print(volume(2))
    print(volume(10))
    print(volume(13.7))
    print(inst(1,2,3))