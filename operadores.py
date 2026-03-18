from math import pow, sqrt
def soma(a, b):
    return a + b
def subtracao(a, b):
    return a - b
def multiplicacao(a, b):
    return a * b
def divisao(a, b):
    if b == 0:
        return 'Divisão por 0 não pode!'
    else:
        return a / b
def potencia(a, b):
    return pow(a, b)
def raiz(a):
    return sqrt(a)
def divinteira(a, b):
    if b  == 0:
        return 'Divisão por 0 não pode!'
    else:
        return a // b
