from Controller.usuarioController import usuarioController
import Model.funcionario


class telaAdmin:
    def tela(admin, listaFuncionarios):
        print(10*'-'+' Tela Principal do Administrador '+'-'*10)
        while True:
            print('1 - Cadastrar Funcionário')
            print('2 - Remover Funcionário')
            print('3 - Editar permissão do funcionário')
            print('4 - Ver dados do Funcionário')
            print('5 - Logout ')
            acao = int(input('O que deseja fazer? '))
            if acao == 1:
                print('Insira seus dados abaixo:')
                nome = input('Digite o nome completo do funcionário: ')
                genero = input(
                    'Digite o gênero do funcionário (M/F): ').upper()
                genero = usuarioController.verificarGenero(genero)
                cpf = input('Digite o cpf do funcionário: ')
                cpf = usuarioController.verificarCpf(listaFuncionarios, cpf)
                idade = int(input('Digite a idade do funcionário: '))
                if usuarioController.verificarIdade(idade) is None:
                    break
                senha = input('Digite a senha do funcionário: ')
                confirmarSenha = input(
                    'Confirme novamente a senha do funcionário por favor: ')
                senha = usuarioController.verificarSenha(senha, confirmarSenha)
                permissao = input(
                    'O funcionário será um administrador do sistema (S/N)? ').upper()
                permissao = usuarioController.verificarSN(permissao)
                cadastro = Model.funcionario.Funcionario(
                    nome, cpf, senha, genero, idade, permissao)
                listaFuncionarios.append(cadastro)
                print('Cadastro concluído com sucesso')
            elif acao == 2:
                cpf = input('Insira o CPF da conta que deseja remover: ')
                funcionario = usuarioController.acharPeloCpf(
                    cpf, listaFuncionarios)
                if funcionario is None:
                    print('Funcionário não encontrado')
                elif funcionario == admin:
                    print('Não é possível remover sua própria conta')
                else:
                    verificar = input(
                        f'Deseja realmente remover a conta de {funcionario.getNome()} ? (S/N) ').upper()
                    verificar = usuarioController.verificarSN(verificar)
                    if verificar == 'S':
                        listaFuncionarios.remove(funcionario)
                        print('Conta removida com sucesso!')
            elif acao == 3:
                cpf = input('Insira o CPF da conta que deseja alterar: ')
                funcionario = usuarioController.acharPeloCpf(
                    cpf, listaFuncionarios)
                if funcionario is None:
                    print('Funcionário não encontrado')
                elif funcionario == admin:
                    print('Não é possível alterar sua própria permissão')
                elif funcionario.getPermissao() == 'S':
                    mudar = input(
                        f'Deseja retirar a permissão do funcionário {funcionario.getNome()} ? (S/N)').upper()
                    mudar = usuarioController.verificarSN(mudar)
                    if mudar == 'S':
                        funcionario.setPermissao('N')
                else:
                    mudar = input(
                        f'Deseja dar permissão ao funcionário {funcionario.getNome()} ? (S/N)').upper()
                    mudar = usuarioController.verificarSN(mudar)
                    if mudar == 'S':
                        funcionario.setPermissao('S')
            elif acao == 4:
                cpf = input(
                    'Digite o CPF do Funcionário que voce quer ver os dados: ')
                funcionario = usuarioController.acharPeloCpf(
                    cpf, listaFuncionarios)
                if funcionario is None:
                    print('Funcionário não encontrado')
                else:
                    print(47 * '-')
                    print(f'Nome: {funcionario.getNome()}\n'
                          f'CPF: {funcionario.getCpf()}\n'
                          f'Genero: {funcionario.getGenero()}\n'
                          f'Possui permissão ? {funcionario.getPermissao()}')
                    print(47 * '-')
            elif acao == 5:
                break
