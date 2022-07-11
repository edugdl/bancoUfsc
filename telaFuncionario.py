def cadastrarNovoUsuario(listaPessoas):
    print('Insira seus dados abaixo:')
    nome = input('Digite seu nome completo: ')
    genero = input('Digite seu gênero (M/F): ').upper()
    while genero not in ['M', 'F']:
        genero = input('Insira seu gênero corretamente: ')
    cpf = input('Digite seu cpf: ')
    while len(cpf) != 11:
        cpf =input('Insira um cpf válido: ')
    while len([i for i in listaPessoas if i.cpf == cpf]) != 0:
        cpf =input('Insira um cpf ainda não cadastrado: ')
    idade = int(input('Digite sua idade: '))
    if idade < 18:
        print('Não é possível criar uma conta sendo menor de idade')
        return None
    senha = input('Digite sua senha: ')
    confirmarSenha = input('Confirme novamente sua senha por favor: ')
    while senha != confirmarSenha:
        print('Senha e Confirmar Senha são diferentes!')
        senha = input('Digite sua senha: ')
        confirmarSenha = input('Confirme novamente sua senha por favor: ')
    return nome,genero,cpf,idade,senha
    

def tela(funcionario):
    print(10*'-'+' Tela Principal do Funcionário '+'-'*10)
    while True:
        print('1 - Abrir conta para um usuário')
        print('2 - Verificar histórico de um usuário')
        print('5 - Logout ')
        acao = int(input('O que deseja fazer? '))
        if acao == 1:
            cadastro = cadastrarNovoUsuario(funcionario.getListaPessoas())
            
            if cadastro is None:
                break
            else:
                nome,genero,cpf,idade,senha = cadastro
                funcionario.cadastrarUsuario(nome,cpf,senha,genero,idade)
                print('Cadastro concluído com sucesso')
        if acao == 2:
            cpf = input('Insira o cpf do usuário que deseja recuperar o histórico: ')
            for usuario in funcionario.getListaPessoas():
                if(usuario.getCpf() == cpf):
                    print('-'*47)
                    print(f'Histórico do usuário {usuario.getNome()}\n')
                    historico = usuario.getContaBancaria().getHistorico()
                    if len(historico) == 0:
                        print('Ainda não foi realizada nenhuma transação')
                    else:
                        for hist in historico:
                            print(f"Foi realizado um {hist['acao']} no valor de R$ {hist['valor']} no dia {hist['data']}")
                    print('-'*47)
        elif acao == 5:
            break