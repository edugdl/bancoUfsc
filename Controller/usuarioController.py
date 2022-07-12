class usuarioController:

    def verificarGenero(genero):
        while genero not in ['M', 'F']:
            genero = input('Insira seu gênero corretamente: ')
        return genero

    def verificarCpf(listaPessoas,cpf):
        while len(cpf) != 11:
            cpf = input('Insira um cpf válido: ')
        while len([i for i in listaPessoas if i.cpf == cpf]) != 0:
            cpf = input('Insira um cpf ainda não cadastrado: ')
        return cpf
    
    def verificarIdade(idade):
        if idade < 18:
            print('Não é possível criar uma conta sendo menor de idade')
            return None
        return idade
    
    def verificarSenha(senha,confirmarSenha):
        while senha != confirmarSenha:
            print('Senha e Confirmar Senha são diferentes!')
            senha = input('Digite sua senha: ')
            confirmarSenha = input('Confirme novamente sua senha por favor: ')
        return senha

    def cadastrarUsuario(funcionario,nome,cpf,senha,genero,idade,conta):
        usuarioCadastrado = funcionario.cadastrarUsuario(nome,cpf,senha,genero,idade,conta)
        return usuarioCadastrado

    def acharPeloCpf(cpf,listaPessoas):
        for pessoa in listaPessoas:
            if pessoa.getCpf() == cpf:
                return pessoa
        else:
            return None
        