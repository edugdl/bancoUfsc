from datetime import datetime
from Controller.usuarioController import usuarioController
from Model.contaBancaria import contaBancaria

class telaFuncionario:
    def tela(funcionario,listaPessoas):
        print(10*'-'+' Tela Principal do Funcionário '+'-'*10)
        while True:
            print('1 - Abrir conta para um usuário')
            print('2 - Verificar histórico de um usuário')
            print('3 - Remover a conta de um usuário')
            print('5 - Logout ')
            acao = int(input('O que deseja fazer? '))
            if acao == 1:
                print('Insira seus dados abaixo:')
                nome = input('Digite seu nome completo: ')
                genero = input('Digite seu gênero (M/F): ').upper()
                genero = usuarioController.verificarGenero(genero)
                cpf = input('Digite seu cpf: ')
                cpf = usuarioController.verificarCpf(listaPessoas,cpf)
                idade = datetime(input('Digite sua idade (ano)-(mes)-(dia) : '))
                if usuarioController.verificarIdade(idade) is None:
                    break
                senha = input('Digite sua senha: ')
                confirmarSenha = input('Confirme novamente sua senha por favor: ')
                senha = usuarioController.verificarSenha(senha,confirmarSenha)
                conta  = contaBancaria(0,'Standard','')
                cadastro = usuarioController.cadastrarUsuario(funcionario,nome,cpf,senha,genero,idade,conta)
                listaPessoas.append(cadastro)
                print('Cadastro concluído com sucesso')
            elif acao == 2:
                cpf = input('Insira o cpf do usuário que deseja recuperar o histórico: ')
                usuario = usuarioController.acharPeloCpf(cpf,listaPessoas)
                if usuario is None:
                    print('Usuário não encontrado')
                else:
                    print('-'*47)
                    print(f'Histórico do usuário {usuario.getNome()}\n')
                    historico = usuario.getContaBancaria().getHistorico()
                    if len(historico) == 0:
                        print('Ainda não foi realizada nenhuma transação')
                    else:
                        for hist in historico:
                            print(f"Foi realizado um(a) {hist['acao']} no valor de R$ {hist['valor']} no dia {hist['data']}")
                    print('-'*47)
            elif acao == 3:
                cpf = input('Insira o CPF da conta que deseja remover: ')
                usuario = usuarioController.acharPeloCpf(listaPessoas,cpf)
                verificar = input(f'Deseja realmente remover a conta de {usuario.getNome()} ? (S/N) ').upper()
                if verificar == 'S':
                    listaPessoas.remove(usuario)
            elif acao == 5:
                break