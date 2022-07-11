def situacaoAtual(usuario):
    print(47 * '-')
    print('Status =', usuario.getContaBancaria().getStatus())
    print('Saldo = R$', usuario.getContaBancaria().getSaldo())
    print(47 * '-')

def tela(usuario):
    print(10*'-'+' Tela Principal do Usuário '+'-'*10)
    while True:
        print('1 - Verificar Situação da Conta')
        print('2 - Realizar Depósito')
        print('3 - Realizar Saque')
        print('4 - Realizar Empréstimo')
        print('5 - Logout ')
        acao = int(input('O que deseja fazer? '))
        if acao == 1:
            situacaoAtual(usuario)
        elif acao == 2:
            valor = float(input('Insira quanto deseja depositar: '))
            usuario.getContaBancaria().depositar(valor)
            print(f'R$ {valor} depositado com sucesso em sua conta !')
            situacaoAtual(usuario)
        elif acao == 3:
            valor = float(input('Insira quanto deseja sacar: '))
            usuario.getContaBancaria().sacar(valor)
            print(f'R$ {valor} sacados com sucesso da sua conta')
            situacaoAtual(usuario)
        elif acao == 4:
            ...
        else:
            print(47 * '-')
            break