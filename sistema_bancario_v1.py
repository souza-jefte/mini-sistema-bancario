#--**--Configurações do Micro Sistema bancário--**--
#Limite de saque diário
LIMITE = 500.0
#Total de saques que é possivel realizar por dia no sistema
TOTAL_SAQUES = 3
#Saldo inical na conta do cliente
saldo = 0
#variavel contadora de saques por dia
saques_qnt = 0
#Quantia total de dinheiro sacado pelo cliente 
saques_feitos = 0
extrato = ''
menu = '''
#######################
# MENU DO SISTEMA BANCÁRIO #
[d]- Fazer depósito
[s]- Fazer saque
[e]- Mostrar Extrato
[q]. Sair
#########################
Por favor, escolha uma opção:
'''
opcao = ''

while opcao != 'q': #Em um loop while, o programa aguarda a entrada do usuário no menu e verifica qual a opção escolhida.
    opcao = input(menu)
    #Se for 'd', o programa solicita um valor para depósito, adiciona ao saldo e atualiza as variáveis de depositos.
    if opcao == 'd':
        valor = float(input("Valor a depositar em R$: "))
        if valor > 0:
            saldo +=valor
            extrato += f'#Depósito: R${valor:.2f}#\n'
        else:
            print("Não aceitamos valores Negativos. Tente Novamente!")
    #Se for 's' e a quantidade de saques realizados for menor que o total permitido, o programa realiza o saque do valor informado e atualiza as variáveis.
    elif opcao == 's' and saques_qnt < TOTAL_SAQUES:
        saque = float(input("Valor a sacar em R$: "))
        if saldo >= saque and saque > 0 :
            if saque <= LIMITE:
                saldo -= saque
                saques_qnt += 1
                extrato += f'#Saque: R${saque:.2f}   #\n'
            else:
                print(f'1. Erro ao exceder limite de R${LIMITE:.2f} para SAQUE')
        else:
            print("Erro por falta de saldo ou saque de valores negativos")
    #Se for 'e', exibe um extrato com informações de depósitos, saques e saldo.
    elif opcao == 'e':
        if len(extrato) > 0 or saques_feitos > 0:
            print('\n#####EXTRATO#####')
            extrato += f'#Saldo R${saldo:.2f}   #\n'
            print(extrato)
        else:
            print('Não foram realizadas movimentações')
    #Se for 'q', o loop termina e se encerra o sistema.
    elif opcao == 'q':
        print('Saindo do sistema..')
    else:
        print('Opcão Invalida, Tente Novamente!')
