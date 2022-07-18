from Model.contaBancaria import contaPoupanca, contaBancaria
from Model.usuario import Usuario
from Model.funcionario import Funcionario


def existeUsuarioCadastrado(cpf, senha, listaGeral):
    for pessoa in listaGeral:
        if pessoa.cpf == cpf and pessoa.senha == senha:
            return pessoa
    else:
        print('Cpf e/ou senha incorretos!')
        return False

def existeUsuarioNasDuasListas(cpf,listaGeral):
    contador = 0
    for pessoa in listaGeral:
        if pessoa.cpf == cpf:
            contador += 1
    return contador

listaUsuarios = list()
listaFuncionarios = list()
listaAdmin = list()
conta = contaBancaria(4500.00, 'conta1')
conta2 = contaBancaria(0, 'conta2')
conta3 = contaPoupanca(1000, 'testePoupanca')
conta4 = contaPoupanca(2000, "micaelRendeDinheiro")
eduardo = Usuario('Eduardo', 'a', '1', 'M', 18, 1000)
eduardo.adicionarContaBancaria(conta)
eduardo.adicionarContaBancaria(conta3)
micael = Usuario('Micael', 'c', '3', 'M', 20, 2000)
micael.adicionarContaBancaria(conta2)
micael.adicionarContaBancaria(conta4)
manuella = Funcionario('Manuella', 'b', '2', 'F', 18,'S')
manuella2 = Usuario('Manuella', 'b', '2', 'F', 18,1000)
print('Olá, Bem-vindo(a) ao Banco')
listaUsuarios.append(eduardo)
listaUsuarios.append(micael)
listaFuncionarios.append(manuella)
listaUsuarios.append(manuella2)


def main():
    while True:
        listaGeral = list()
        listaGeral.extend(listaUsuarios)
        listaGeral.extend(listaFuncionarios)
        listaGeral.extend(listaAdmin)
        print('1 - Login')
        print('2 - Sair')
        acao = int(input('O que deseja fazer? '))
        if acao == 1:
            cpf = input('Insira seu cpf: ')
            senha = input('Insira sua senha: ')
            login = existeUsuarioCadastrado(cpf, senha, listaGeral)
            while not login:
                print('Caso queira sair insira o cpf como 0')
                cpf = input('Insira novamente seu cpf: ')
                if cpf == '0':
                    break
                senha = input('Insira novamente sua senha: ')
                login = existeUsuarioCadastrado(cpf, senha, listaGeral)
            if existeUsuarioNasDuasListas(cpf,listaGeral) > 1:
                print(f'Olá {login.nome}')
                acesso = int(input('1-Usuário\n2-Funcionário\nInsira como deseja acessar: '))
                if acesso == 1:
                    login = existeUsuarioCadastrado(cpf,senha,listaUsuarios)
                    login.abrirTela(listaUsuarios)
                elif acesso == 2:
                    login = existeUsuarioCadastrado(cpf,senha,listaFuncionarios)
                    if login.getPermissao() == 'S':
                        login.abrirTela(listaFuncionarios,listaUsuarios)
                    else:
                        login.abrirTela(listaUsuarios)
            elif login in listaFuncionarios:
                if login.getPermissao() == 'S':
                    print(f'Olá {login.nome}')
                    login.abrirTela(listaFuncionarios,listaUsuarios)
                else:
                    print(f'Olá {login.nome}')
                    login.abrirTela(listaFuncionarios,listaUsuarios)
            elif cpf != '0':
                print(f'Olá {login.nome}')
                login.abrirTela(listaUsuarios)
        elif acao == 2:
            break


if __name__ == '__main__':
    main()
