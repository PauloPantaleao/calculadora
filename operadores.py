def soma(a, b):
    so = a + b
    return so
def subtracao(a, b):
    su = a - b
    return su
def multiplicacao(a, b):
    mu = a * b
    return mu
def divisao(a, b):
    if b  == 0:
        return 'Divisão por 0 não pode!'
    di = a / b
    return di
def potencia(a, b):
    from math import pow
    po = pow(a, b)
    return po
def raiz(a):
    from math import sqrt
    r = sqrt(a)
    return r
def divinteira(a, b):
    if b  == 0:
        return 'Divisão por 0 não pode!'
    divi = a // b
    return divi

