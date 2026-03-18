def line():
    print('-' * 30)
def title(msg):
    print(f'{str(msg):^30}') 
def menu():
    return """
SELECIONE QUAL OPERAÇÃO DESEJA REALIZAR:
[ 1 ] SOMA
[ 2 ] SUBTRAÇÃO
[ 3 ] MULTIPLICAÇÃO
[ 4 ] DIVISÃO
[ 5 ] DIVISÃO INTEIRA 
[ 6 ] POTÊNCIA
[ 7 ] RAIZ QUADRADA
"""
def processo():
    return 'PROCESSANDO OPERAÇÃO...'

