from Model.contaBancaria import contaPoupanca, contaBancaria


class contaBancariaController:
    def depositar(conta, deposito):
        if deposito > 0:
            return conta.depositar(deposito)
        return None

    def sacar(conta, saque):
        if saque <= 0:
            return -1
        if conta.getSaldo() < saque:
            return 0
        return conta.sacar(saque)

    def transferir(manda, recebePessoa, valor):
        print('Escolha abaixo a conta que irá receber o dinheiro')
        recebe = contaBancariaController.selecionarConta(recebePessoa)
        if manda.getSaldo() < valor:
            return None
        else:
            manda.transferir(recebe, valor)
            return recebePessoa

    def criarConta(usuario, tipoDeConta, saldo, nomeDaConta):
        if tipoDeConta == 'C':
            novaConta = contaBancaria(saldo, nomeDaConta)
        else:
            novaConta = contaPoupanca(saldo, nomeDaConta)
        usuario.adicionarContaBancaria(novaConta)

    def selecionarConta(usuario):
        if len(usuario.getListaContaBancaria()) == 1:
            return usuario.getListaContaBancaria()[0]
        for i, contaBancaria in enumerate(usuario.getListaContaBancaria()):
            print(f'{i+1} - {contaBancaria.getNomeConta()}')
        contaEscolhida = int(
            input('Digite a conta que deseja selecionar: ')) - 1
        return usuario.getListaContaBancaria()[contaEscolhida]
