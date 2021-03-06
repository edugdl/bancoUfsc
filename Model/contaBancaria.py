from datetime import datetime, timedelta


class contaBancaria:
    def __init__(self, saldo, nomeConta):
        self.saldo = saldo
        self.historico = []
        self.nomeConta = nomeConta
        self.dataUltimaAtualizacao = datetime.now()
        self.emprestimoAtual = False

    def atualizar(self):
        diferenca = int(((datetime.now() - self.dataUltimaAtualizacao).seconds)/60)
        if diferenca > 0:
            if self.emprestimoAtual:
                valorDebito = self.emprestimoAtual['valorInicial'] * (1.03 ** self.emprestimoAtual['vezAtual'])
                self.adicionarNoHistorico('Débito empréstimo', valorDebito)
                self.saldo -= valorDebito
                self.emprestimoAtual['vezAtual'] += 1
                if self.emprestimoAtual['vezAtual'] == self.emprestimoAtual['vezes']:
                    self.emprestimoAtual = False
            self.saldo -= 5
            if self.saldo < 0:
                self.saldo *= 1.01 ** diferenca
            self.dataUltimaAtualizacao += timedelta(minutes=diferenca)
        return self.saldo

    def getNomeConta(self):
        return self.nomeConta

    def setNomeConta(self, nomeConta):
        self.nomeConta = nomeConta

    def getTipoConta(self):
        return 'Conta Corrente'

    def getSaldo(self):
        self.atualizar()
        return self.saldo

    def getSaldoFormatado(self):
        saldo = f'{self.getSaldo():.2f}'
        return saldo

    def adicionarNoHistorico(self, acaoV, valorV):
        dataAtual = datetime.now()
        dataHora = dataAtual.strftime('%d/%m/%Y às %H:%M:%S')
        if(len(self.historico)) == 5:
            self.historico.pop(4)
        dicionarioHistorico = {'data': dataHora,
                               'acao': acaoV, 'valor': valorV}
        self.historico.insert(0, dicionarioHistorico)

    def depositar(self, deposito):
        self.atualizar()
        self.adicionarNoHistorico('Depósito', deposito)
        self.saldo += deposito
        return deposito

    def sacar(self, saque):
        self.atualizar()
        self.adicionarNoHistorico('Saque', saque)
        self.saldo -= saque
        return saque

    def transferir(self, recebe, valor):
        self.atualizar()
        recebe.atualizar()
        self.saldo -= valor
        self.adicionarNoHistorico('Transferência (-)', valor)
        recebe.saldo += valor
        recebe.adicionarNoHistorico('Transferência (+)', valor)

    def getStatus(self):
        self.atualizar()
        if float(self.getSaldoFormatado()) > 0:
            return 'Positiva'
        elif float(self.getSaldoFormatado()) == 0:
            return 'Zerada'
        return 'Negativa'

    def getHistorico(self):
        return self.historico

    def emprestimo(self,emprestimo):
        emprestimoConta = emprestimo['valorInicial'] * emprestimo['vezes']
        self.adicionarNoHistorico('Empréstimo', emprestimoConta)
        self.saldo += emprestimoConta
        self.emprestimoAtual = emprestimo


class contaPoupanca(contaBancaria):
    def __init__(self, saldo, nomeConta):
        super().__init__(saldo, nomeConta)

    def atualizar(self):
        diferenca = int(((datetime.now() - self.dataUltimaAtualizacao).seconds) / 60)
        if diferenca > 0:
            self.saldo *= 1.005 ** diferenca
            self.dataUltimaAtualizacao += timedelta(minutes=diferenca)
        return self.saldo

    def getTipoConta(self):
        return "Conta Poupança"
