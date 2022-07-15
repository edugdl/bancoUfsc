class usuarioController:

    def verificarGenero(genero):
        while genero not in ['M', 'F']:
            genero = input('Insira o gênero  do usuário corretamente (M/F): ').upper()
        return genero

    def verificarCpf(listaPessoas, cpf):
        while len(cpf) != 11:
            cpf = input('Insira um cpf válido: ')
        while len([i for i in listaPessoas if i.getCpf() == cpf]) != 0:
            cpf = input('Insira um cpf ainda não cadastrado: ')
        return cpf

    def verificarIdade(idade):
        if idade < 18:
            print('Não é possível criar uma conta sendo menor de idade')
            return None
        return idade

    def verificarSenha(senha, confirmarSenha):
        while senha != confirmarSenha:
            print('Senha e Confirmar Senha são diferentes!')
            senha = input('Digite a senha do usuário: ')
            confirmarSenha = input('Confirme novamente a senha do usuário por favor: ')
        return senha

    def verificarConta(conta):
        while not conta in ['C', 'P']:
            print('Tipo de conta incorreta, digite novamente!')
            conta = input(
                'Qual o tipo de conta? C - Corrente, P - Poupança').upper()
        return conta

    def verificarSN(opcao):
        while opcao not in ['S','N']:
            opcao = input('Digite corretamente a opção (S/N): ').upper()
        return opcao

    def acharPeloCpf(cpf, listaPessoas):
        for pessoa in listaPessoas:
            if pessoa.getCpf() == cpf:
                return pessoa
        else:
            return None

    def removerContaBancaria(usuario,contaEscolhida):
        listaConta = usuario.getListaContaBancaria()
        listaConta.remove(contaEscolhida)
        usuario.setListaContaBancaria(listaConta)