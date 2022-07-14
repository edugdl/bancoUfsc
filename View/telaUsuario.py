import Controller.contaBancariaController as contaBancariaController
from Controller.usuarioController import *


class telaUsuario:
    def situacaoAtual(contaEscolhida):
        print(47 * '-')
        print('Status =', contaEscolhida.getStatus())
        print('Saldo = R$', contaEscolhida.getSaldoFormatado())
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
                if contaEscolhida is None:
                    print('Peça a um dos atendentes para criar uma conta em seu nome')
                    break
                telaUsuario.situacaoAtual(contaEscolhida)
            elif acao == 2:
                contaEscolhida = contaBancariaController.selecionarConta(
                    usuario)
                if contaEscolhida is None:
                    print('Peça a um dos atendentes para criar uma conta em seu nome')
                    break
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
                if contaEscolhida is None:
                    print('Peça a um dos atendentes para criar uma conta em seu nome')
                    break
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
                contaEscolhida = contaBancariaController.selecionarConta(
                    usuario)
                if type(contaEscolhida).__name__ == 'contaPoupanca':
                    print('Não é possível realizar empréstimo em contas poupança!')
                elif contaEscolhida.emprestimoAtual:
                    print('Não é possível realizar empréstimo com outro em andamento')
                elif contaEscolhida is None:
                    print('Peça a um dos atendentes para criar uma conta em seu nome')
                    break
                else:
                    valorEmprestimo = float(input('Digite o valor do empréstimo: '))
                    salario = input(f'Seu salário continua sendo {usuario.getSalario()} ? (S/N): ').upper()
                    salario = usuarioController.verificarSN(salario)
                    if salario == 'N':
                        salario = float(input('Digite seu novo salário: '))
                        usuario.setSalario(salario)
                    listaEmprestimo = contaBancariaController.verificarEmprestimo(valorEmprestimo,usuario.getSalario())
                    if len(listaEmprestimo) == 0:
                        print(f'Não é possível realizar um empréstimo de valor R$ {valorEmprestimo:.2f} em até 12x')
                    else:
                        for i,emprestimo in enumerate(listaEmprestimo):
                            print(f'{i+1} - {emprestimo["vezes"]}x resultado em um total de {emprestimo["total"]:.2f}')
                        escolhaEmprestimo = int(input('Escolha uma opção de empréstimo: '))
                        contaBancariaController.emprestimo(contaEscolhida,listaEmprestimo[escolhaEmprestimo-1])
            elif acao == 5:
                contaEscolhida = contaBancariaController.selecionarConta(
                    usuario)
                if contaEscolhida is None:
                    print('Peça a um dos atendentes para criar uma conta em seu nome')
                    break
                pessoaRecebe = input(
                    'Insira o CPF da pessoa a qual deseja realizar a transferência: ')
                recebe = usuarioController.acharPeloCpf(
                    pessoaRecebe, listaPessoas)
                if recebe is None:
                    print('Usuário não encontrado')
                else:
                    valor = float(
                        input('Insira o valor o qual deseja transferir: '))
                    transferencia = contaBancariaController.transferir(
                        contaEscolhida, recebe, valor)
                    if transferencia:
                        print(
                            f'Transferência de {usuario.getNome()} para {transferencia.getNome()} no valor de R$ {valor:.2f} concluída com sucesso!')
                    elif transferencia is None:
                        print('Saldo na conta insuficiente')
                    else:
                        print('A pessoa selecionada não possui uma conta')
            elif acao == 6:
                contaEscolhida = contaBancariaController.selecionarConta(
                    usuario)
                if contaEscolhida is None:
                    print('Peça a um dos atendentes para criar uma conta em seu nome')
                    break
                historico = contaEscolhida.getHistorico()
                print('-'*47)
                print(f'Histórico de {contaEscolhida.getNomeConta()}\n')
                if len(historico) == 0:
                    print('Ainda não foi realizada nenhuma transação')
                else:
                    for hist in historico:
                        print(
                            f"Foi realizado um(a) {hist['acao']} no valor de R$ {hist['valor']:.2f} no dia {hist['data']}")
                print('-'*47)
            elif acao == 7:
                print(47 * '-')
                break
