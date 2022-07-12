from datetime import datetime


class contaBancaria:
    def __init__(self, saldo, nomeConta):
        self.saldo = saldo
        self.historico = []
        self.nomeConta = nomeConta

    def getNomeConta(self):
        return self.nomeConta

    def setNomeConta(self, nomeConta):
        self.nomeConta = nomeConta

    def getTipoConta(self):
        return 'Conta Corrente'

    def getSaldo(self):
        return self.saldo

    def adicionarNoHistorico(self, acaoV, valorV):
        dataAtual = datetime.now()
        dataHora = dataAtual.strftime('%d/%m/%Y às %H:%M:%S')
        if(len(self.historico)) == 5:
            self.historico.pop(4)
        dicionarioHistorico = {'data': dataHora,
                               'acao': acaoV, 'valor': valorV}
        self.historico.insert(0, dicionarioHistorico)

    def depositar(self, deposito):
        self.adicionarNoHistorico('Depósito', deposito)
        self.saldo += deposito
        return deposito

    def sacar(self, saque):
        self.adicionarNoHistorico('Saque', saque)
        self.saldo -= saque

    def transferir(self, recebe, valor):
        self.saldo -= valor
        self.adicionarNoHistorico('Transferência (-)', valor)
        recebe.saldo += valor
        recebe.adicionarNoHistorico('Transferência (+)', valor)

    def getStatus(self):
        if self.saldo > 0:
            return 'Positiva'
        elif self.saldo == 0:
            return 'Zerada'
        return 'Negativa'

    def getHistorico(self):
        return self.historico


class contaPoupanca(contaBancaria):
    def __init__(self, saldo, nomeConta):
        super().__init__(saldo, nomeConta)

    def atualizar(self):
        ...

    def getTipoConta(self):
        return "Conta Poupança"
