from Model.contaBancaria import contaPoupanca, contaBancaria

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
    recebe = selecionarConta(recebePessoa)
    if recebe is None:
        print('A pessoa selecionada não possui uma conta')
        return False
    if valor < 0:
        print('Valor de transferência inválido')
        return False
    if manda.getSaldo() < valor:
        print('Saldo na conta insuficiente')
        return False
    manda.transferir(recebe, valor)
    return recebePessoa

def criarConta(usuario, tipoDeConta, saldo, nomeDaConta):
    if tipoDeConta == 'C':
        novaConta = contaBancaria(saldo, nomeDaConta)
    else:
        novaConta = contaPoupanca(saldo, nomeDaConta)
    usuario.adicionarContaBancaria(novaConta)

def selecionarConta(usuario):
    if len(usuario.getListaContaBancaria()) == 0:
        return None
    elif len(usuario.getListaContaBancaria()) == 1:
        return usuario.getListaContaBancaria()[0]
    for i, contaBancaria in enumerate(usuario.getListaContaBancaria()):
        print(f'{i+1} - {contaBancaria.getNomeConta()}')
    contaEscolhida = int(
        input('Digite a conta que deseja selecionar: ')) - 1
    return usuario.getListaContaBancaria()[contaEscolhida]

def verificarEmprestimo(valor,salario):
    listaPrestacoes = []
    for i in range(3,13):
        if ((valor/i) * (1.03**i)) <= salario * 0.3:
            total = 0
            for j in range(1,i+1):
                total += (valor/i) * (1.03 ** j)
            listaPrestacoes.append({'valorInicial':valor/i,'vezes':i,'vezAtual':1,'total':total})
    
    return listaPrestacoes

def emprestimo(contaBancaria,emprestimo):
    for i in range(1,emprestimo['vezes']+1):
        print(f'Parcela {i} - R$ {(emprestimo["valorInicial"]) * (1.03 ** i):.2f}')
    print('Empréstimo realizado com sucesso!')
    return contaBancaria.emprestimo(emprestimo)