from datetime import datetime

class contaBancaria:
    def __init__(self, saldo, tipoDeConta, Acoes):
        self.saldo = saldo
        self.tipoDeConta = tipoDeConta
        self.Acoes = Acoes
        self.historico = []

    def getSaldo(self):
        return self.saldo
    
    def adicionarNoHistorico(self,acaoV,valorV):
        dataAtual = datetime.now()
        dataHora = dataAtual.strftime('%d/%m/%Y às %H:%M:%S')
        if(len(self.historico)) == 5:
            self.historico.pop(4)
        dicionarioHistorico = {'data':dataHora,'acao': acaoV , 'valor': valorV}
        self.historico.insert(0,dicionarioHistorico)

    def depositar(self, deposito):
        self.adicionarNoHistorico('Depósito',deposito)
        self.saldo += deposito

    def sacar(self,saque):
        self.adicionarNoHistorico('Saque',saque)
        self.saldo -= saque

    def getTipodeconta(self):
        return self.tipoDeConta

    def setTipodeconta(self, tipoDeConta):
        self.tipoDeConta = tipoDeConta

    def getAcoes(self):
        return self.Acoes

    def setAcoes(self, Acoes):
        self.Acoes = Acoes

    def getStatus(self):
        if self.saldo > 0:
            return 'Positiva'
        elif self.saldo == 0:
            return 'Zerada'
        return 'Negativa'
    
    def getHistorico(self):
        return self.historico
        
        
    