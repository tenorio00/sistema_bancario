MENU = """

[d]depositar
[s]sacar
[e]extrato
[q]sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITES_SAQUES = 3

opcao = input(MENU)

if opcao == 'd':
    valor = float(input('Informe o valor do deposito : '))
       
    if valor > 0:
        saldo += valor
        extrato += f'Deposito: R${valor:.2f}\n'
    else:
        print('Operação falhou! O valor informado é invalido.')

elif opcao == 's':
    valor = float(input('Informe o valor do saque : '))

    excedeu_saldo = valor > saldo

    excedeu_limite = valor > limite

    excedeu_saques = numero_saques >= LIMITES_SAQUES

    if excedeu_saldo :
        print('Operação flhou você não tem saldo suficiente.')
    
    elif excedeu_limite:
        print('')
        
