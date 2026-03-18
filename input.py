import operadores
import escrita
from time import sleep
escrita.line()
escrita.title('BEM VINDO!')
escrita.line()
primeironum = float(input('Digite o primeiro valor do calculo: '))
escrita.line()
print(escrita.menu(), end='\n')
escrita.line()
escolha = -1
while escolha not in range(1, 8):
    escolha = int(input())
escrita.line()
print(escrita.processo())
sleep(2)
escrita.line()
if escolha == 7:
    print(f'A raiz quadrada de {primeironum} é {operadores.raiz(primeironum)}')
else:
    segundonum = float(input('Digite o segundo valor do calculo: '))
    if escolha == 1:
        print(f'A soma de {primeironum} e {segundonum} é {operadores.soma(primeironum, segundonum)}')
    elif escolha == 2:
        print(f'A subtração de {primeironum} por {segundonum} é {operadores.subtracao(primeironum, segundonum)}')
    elif escolha == 3:
        print(f'A multiplicação de {primeironum} e {segundonum} é {operadores.multiplicacao(primeironum, segundonum)}')
    elif escolha == 4:
        print(f'A divisão entre {primeironum} e {segundonum} é {operadores.divisao(primeironum, segundonum)}')
    elif escolha == 5:
        print(f'A divisão inteira entre {primeironum} e {segundonum} é {operadores.divinteira(primeironum, segundonum)}')
    elif escolha == 6:
        print(f'A potência de {primeironum} elevado por {segundonum} é {operadores.potencia(primeironum, segundonum)}')
    else:
        print('ERRO.')
escrita.line()
escrita.title('FIM')
escrita.line()
