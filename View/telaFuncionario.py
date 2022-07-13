from datetime import datetime
from Controller.contaBancariaController import contaBancariaController
from Controller.usuarioController import usuarioController
from Model.contaBancaria import contaBancaria


class telaFuncionario:
    def tela(funcionario, listaPessoas):
        print(10*'-'+' Tela Principal do Funcionário '+'-'*10)
        while True:
            print('1 - Cadastrar Usuário')
            print('2 - Verificar histórico de um usuário')
            print('3 - Remover a conta de um usuário')
            print('4 - Abrir uma conta bancária para o usuário')
            print('5 - Logout ')
            acao = int(input('O que deseja fazer? '))
            if acao == 1:
                print('Insira seus dados abaixo:')
                nome = input('Digite o nome completo do usuário: ')
                genero = input('Digite o gênero do usuário (M/F): ').upper()
                genero = usuarioController.verificarGenero(genero)
                cpf = input('Digite o cpf do usuário: ')
                cpf = usuarioController.verificarCpf(listaPessoas, cpf)
                idade = int(input('Digite a idade do usuário: '))
                if usuarioController.verificarIdade(idade) is None:
                    break
                senha = input('Digite a senha do usuário: ')
                confirmarSenha = input(
                    'Confirme novamente a senha do usuário por favor: ')
                senha = usuarioController.verificarSenha(senha, confirmarSenha)
                cadastro = usuarioController.cadastrarUsuario(
                    funcionario, nome, cpf, senha, genero, idade)
                listaPessoas.append(cadastro)
                print('Cadastro concluído com sucesso')
            elif acao == 2:
                cpf = input(
                    'Insira o cpf do usuário que deseja recuperar o histórico: ')
                usuario = usuarioController.acharPeloCpf(cpf, listaPessoas)
                if usuario is None:
                    print('Usuário não encontrado')
                elif contaEscolhida is None:
                    print('Usuário não possui conta cadastrada')
                else:
                    contaEscolhida = contaBancariaController.selecionarConta(
                    usuario)
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
            elif acao == 3:
                cpf = input('Insira o CPF da conta que deseja remover: ')
                usuario = usuarioController.acharPeloCpf(cpf, listaPessoas)
                if usuario is None:
                    print('Usuário não encontrado')
                else:
                    verificar = input(
                        f'Deseja realmente remover a conta de {usuario.getNome()} ? (S/N) ').upper()
                    while verificar not in ['S','N']:
                        print('Digite corretamente por favor')
                        verificar = input(f'Deseja realmente remover a conta de {usuario.getNome()} ? (S/N) ').upper()
                    if verificar == 'S':
                        listaPessoas.remove(usuario)
            elif acao == 4:
                cpf = input(
                    'Digite o CPF do usuário que você quer abrir uma conta: ')
                usuario = usuarioController.acharPeloCpf(cpf, listaPessoas)
                if usuario is None:
                    print('Usuário não encontrado')
                else:
                    tipoConta = input(
                        'Qual o tipo de conta? C - Corrente, P - Poupança: ').upper()
                    tipoConta = usuarioController.verificarConta(tipoConta)
                    saldo = float(
                        input('Insira o saldo que o usuário irá começar na conta: '))
                    nomeConta = input('Digite o nome que o usuário na conta: ')
                    print(
                        f'Conta criada com sucesso para o usuário {usuario.getNome()}!')
                    contaBancariaController.criarConta(usuario, tipoConta, saldo, nomeConta)
            elif acao == 5:
                break
