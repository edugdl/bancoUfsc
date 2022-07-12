from Controller.contaBancariaController import *
from Controller.usuarioController import *


class telaUsuario:
    def situacaoAtual(contaEscolhida):
        print(47 * '-')
        print('Status =', contaEscolhida.getStatus())
        print('Saldo = R$', contaEscolhida.getSaldo())
        print('Tipo de conta = ', contaEscolhida.getTipoConta())
        print(47 * '-')

    def tela(usuario, listaPessoas):
        print(10*'-'+' Tela Principal do Usuário '+'-'*10)
        while True:
            print('1 - Verificar Situação da Conta')
            print('2 - Realizar Depósito')
            print('3 - Realizar Saque')
            print('4 - Realizar Empréstimo')
            print('5 - Realizar Transferência')
            print('6 - Verificar histórico da conta')
            print('7 - Logout ')
            acao = int(input('O que deseja fazer? '))
            if acao == 1:
                contaEscolhida = contaBancariaController.selecionarConta(
                    usuario)
                telaUsuario.situacaoAtual(contaEscolhida)
            elif acao == 2:
                contaEscolhida = contaBancariaController.selecionarConta(
                    usuario)
                valor = float(input('Insira quanto deseja depositar: '))
                retornoDeposito = contaBancariaController.depositar(
                    contaEscolhida, valor)
                if retornoDeposito is None:
                    print("Valor de depósito inválido!")
                else:
                    print(
                        f"Depósito de R$ {retornoDeposito} concluído com sucesso!")
                    telaUsuario.situacaoAtual(contaEscolhida)
            elif acao == 3:
                contaEscolhida = contaBancariaController.selecionarConta(
                    usuario)
                valor = float(input('Insira quanto deseja sacar: '))
                retornoSaque = contaBancariaController.sacar(
                    contaEscolhida, valor)
                if retornoSaque == -1:
                    print('Valor de saque inválido!')
                elif retornoSaque == 0:
                    print('Saldo na conta insuficiente')
                else:
                    print(f'Saque de R$ {valor} concluído com sucesso!')
                    telaUsuario.situacaoAtual(contaEscolhida)
            elif acao == 4:
                ...
            elif acao == 5:
                contaEscolhida = contaBancariaController.selecionarConta(
                    usuario)
                pessoaRecebe = input(
                    'Insira o CPF da pessoa a qual deseja realizar a transferência: ')
                recebe = usuarioController.acharPeloCpf(
                    pessoaRecebe, listaPessoas)
                if recebe is None:
                    print('Usuário não encontrado')
                    break
                valor = float(
                    input('Insira o valor o qual deseja transferir: '))
                transferencia = contaBancariaController.transferir(
                    contaEscolhida, recebe, valor)
                if transferencia:
                    print(
                        f'Transferência de {usuario.getNome()} para {transferencia.getNome()} no valor de R$ {valor} concluída com sucesso!')
                elif transferencia is None:
                    print('Saldo na conta insuficiente')
                else:
                    print('Usuário não encontrado')
            elif acao == 6:
                usuario = usuarioController.acharPeloCpf(
                    usuario.getCpf(), listaPessoas)
                print('-'*47)
                print(f'Seu histórico\n')
                contaEscolhida = contaBancariaController.selecionarConta(
                    usuario)
                historico = contaEscolhida.getHistorico()
                if len(historico) == 0:
                    print('Ainda não foi realizada nenhuma transação')
                else:
                    for hist in historico:
                        print(
                            f"Foi realizado um(a) {hist['acao']} no valor de R$ {hist['valor']} no dia {hist['data']}")
                print('-'*47)
            elif acao == 7:
                print(47 * '-')
                break
