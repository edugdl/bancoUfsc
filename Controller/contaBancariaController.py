class contaBancariaController:
    def depositar(conta,deposito):
        if deposito > 0:
            return conta.depositar(deposito)
        return None

    def sacar(conta,saque):
        if saque <= 0:
            return -1
        if conta.getSaldo() < saque:
            return 0
        return conta.sacar(saque)

    def transferir(manda,recebePessoa,valor,listaPessoas):
        recebe = recebePessoa.getContaBancaria()
        if manda.getSaldo() < valor:
            return None
        else:
            manda.transferir(recebe,valor)
            return recebePessoa
        
