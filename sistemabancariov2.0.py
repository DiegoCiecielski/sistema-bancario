from abc import ABC

class Pessoa:
    def __init__(self, nome, sobrenome, idade, cpf):
         self.nome = nome
         self.sobrenome = sobrenome
         self.idade = idade
         self.__cpf = cpf
         self.__ContaBancarias = []

    def info(self):
        print(f'Nome: {self.nome} {self.sobrenome}, Idade: {int(self.idade)} anos, CPF: {self.__cpf} ')

    def InfoContas(self):
        self.info()
        for conta in self.__ContaBancarias:
            conta.info()

class Banco:
    def __init__(self, nome, cnpj, NroBanco):
        self.__nome = nome
        self.__cnpj = cnpj
        self.__NroBanco = NroBanco
        self.__ContasBancarias = []

    def InfoBanco(self):
        print(f'Informações do Banco:'
              f'Nome do banco: {self.__nome}'
              f'CNPJ: {self.__cnpj}'
              f'Número do banco: {int(self.__NroBanco)}')

    def InfoContas(self):
        print(f'Banco: {self.__nome}, CNPJ: {self.__cnpj}, Número: {self.__NroBanco}')
        for conta in self.__ContasBancarias:
            conta.info()

    def CriarConta(self, conta):
        self.__ContasBancarias.append(conta)

    def FecharConta(self, conta):
        if conta in self.__ContasBancarias:
            self.__ContasBancarias.remove(conta)
            print(f'Conta {conta.NroConta} fechada.')


class ContaBancaria(ABC):
    def __init__(self, titular: Pessoa, banco: Banco, NroConta: int, saldo: float, senha: str):
        self.titular = titular
        self.banco = banco
        self.NroConta = NroConta
        self.saldo = saldo
        self.senha = senha

    def saque(self, valor: float, senha: str):
        pass

    def deposito(self, valor: float):
        pass

    def VerificaSenha(self, senha: str):
        return self.senha == senha

class ContaCorrente(ContaBancaria):
    def __init__(self, titular: Pessoa, banco: Banco, NroConta: int, saldo: float, senha: str, TaxasMensais: float):
        super().__init__(titular, banco, NroConta, saldo, senha)
        self.__TaxasMensais = TaxasMensais

    def saque(self, valor: float, senha: str):
        if self.VerificaSenha(senha):
            if self.saldo >= valor:
                self.saldo -= valor
                print(f'Saque de R${valor:.2f} efetuado. Saldo: R${self.saldo:.2f}')
            else:
                print(f'Saldo insuficiente.')
        else:
            print(f'Senha incorreta')

    def deposito(self, valor: float):
        self.saldo += valor
        print(f'Depósito de R${valor:.2f} efetuado. Saldo: R${self.saldo:.2f}')

    def NovoMes(self):
        if self.saldo >= self.__TaxasMensais:
            self.saldo -= self.__TaxasMensais
        print(f'Taxas mensais {self.__TaxasMensais}. Novo saldo: R${self.saldo:.2f}')

    def info(self):
        print(f'Conta Corrente Nº: {self.NroConta}, Saldo: R${self.saldo:.2f}, Taxas Mensais: {self.__TaxasMensais}% ao mês')
class ContaPoupanca(ContaBancaria):
    def __init__(self, titular: Pessoa, banco: Banco, NroConta: int, saldo: float, senha: str, rendimento: float):
        super().__init__(titular, banco, NroConta, saldo, senha)
        self.__rendimento = rendimento
        self.SaquesMensais = 3

    def saque(self, valor: float, senha: str):
        if self.SaquesMensais <= 0:
            print(f'Limite de saques excedido.')
            return

        if self.VerificaSenha(senha):
            if self.saldo >= valor:
                self.saldo -= valor
                self.SaquesMensais -=1
                print(f'Saque de R${valor:.2f} efetuado. Novo Saldo R${self.saldo:.2f}')
            else:
                print(f'Senha incorreta.')

    def deposito(self, valor: float):
        self.saldo += valor
        print(f'Depósito de R${valor:.2f} efetuado. Novo saldo R${self.saldo:.2f}')

    def NovoMes(self):
        self.saldo += self.saldo * self.__rendimento
        print(f'Rendimento aplicado. Saldo atual: R${self.saldo:.2f}')

    def info(self):
        print(f'Conta Poupança Nº: {self.NroConta}, Saldo: R${self.saldo:.2f}, Rendimento: {self.__rendimento*100}% ao mês')

def menu_principal():
    bancos = []
    pessoas = []

    while True:
        print('\n----- Sistema Bancário -----')
        print('1. Cadastrar Banco')
        print('2. Cadastrar Pessoa')
        print('3. Cadastrar Conta Corrente')
        print('4. Cadastrar Conta Poupança')
        print('5. Consultar Informações de um Banco')
        print('6. Consultar Informações de uma Pessoa')
        print('7. Fechar Conta')
        print('8. Realizar Saque')
        print('9. Realizar Depósito')
        print('10. Novo Mês')
        print('11. Sair')

        opcao = input('Escolha uma opção: ')

        if opcao == '1':
            cadastrar_banco(bancos)
        elif opcao == '2':
            cadastrar_pessoa(pessoas)
        elif opcao == '3':
            cadastrar_conta_corrente(bancos, pessoas)
        elif opcao == '4':
            cadastrar_conta_poupanca(bancos, pessoas)
        elif opcao == '5':
            consultar_informacoes_banco(bancos)
        elif opcao == '6':
            consultar_informacoes_pessoa(pessoas)
        elif opcao == '7':
            fechar_conta(bancos, pessoas)
        elif opcao == '8':
            realizar_saque(pessoas)
        elif opcao == '9':
            realizar_deposito(pessoas)
        elif opcao == '10':
            aplicar_novo_mes(pessoas)
        elif opcao == '11':
            print('Saindo...')
            break
        else:
            print('Opção inválida! Tente novamente.')


def cadastrar_banco(bancos):
    nome = input('Nome do Banco: ')
    cnpj = input('CNPJ do Banco: ')
    numero_banco = int(input('Número do Banco: '))
    banco = Banco(nome, cnpj, numero_banco)
    bancos.append(banco)
    print(f'Banco {nome} cadastrado com sucesso!')


def cadastrar_pessoa(pessoas):
    nome = input('Nome: ')
    sobrenome = input('Sobrenome: ')
    idade = int(input('Idade: '))
    cpf = input('CPF: ')
    pessoa = Pessoa(nome, sobrenome, idade, cpf)
    pessoas.append(pessoa)
    print(f'Pessoa {nome} {sobrenome} cadastrada com sucesso!')


def cadastrar_conta_corrente(bancos, pessoas):
    pessoa = buscar_pessoa(pessoas)
    banco = buscar_banco(bancos)
    if pessoa and banco:
        numero_conta = int(input('Número da Conta Corrente: '))
        saldo = float(input('Saldo Inicial: '))
        senha = input('Senha: ')
        taxas_mensais = float(input('Taxas Mensais: '))
        conta = ContaCorrente(pessoa, banco, numero_conta, saldo, senha, taxas_mensais)
        pessoa._Pessoa__ContaBancarias.append(conta)
        banco._Banco__ContasBancarias.append(conta)
        print(f'Conta Corrente {numero_conta} cadastrada com sucesso para {pessoa.nome} {pessoa.sobrenome} no banco {banco._Banco__nome}!')


def cadastrar_conta_poupanca(bancos, pessoas):
    pessoa = buscar_pessoa(pessoas)
    banco = buscar_banco(bancos)
    if pessoa and banco:
        numero_conta = int(input('Número da Conta Poupança: '))
        saldo = float(input('Saldo Inicial: '))
        senha = input('Senha: ')
        rendimento = float(input('Rendimento Mensal (em %): ')) / 100
        conta = ContaPoupanca(pessoa, banco, numero_conta, saldo, senha, rendimento)
        pessoa._Pessoa__ContaBancarias.append(conta)
        banco._Banco__ContasBancarias.append(conta)
        print(f'Conta Poupança {numero_conta} cadastrada com sucesso para {pessoa.nome} {pessoa.sobrenome} no banco {banco._Banco__nome}!')

def consultar_informacoes_banco(bancos):
    banco = buscar_banco(bancos)
    if banco:
        banco.InfoContas()

def consultar_informacoes_pessoa(pessoas):
    pessoa = buscar_pessoa(pessoas)
    if pessoa:
        pessoa.InfoContas()

def fechar_conta(bancos, pessoas):
    pessoa = buscar_pessoa(pessoas)
    if pessoa:
        conta_numero = int(input('Número da Conta a ser fechada: '))
        conta = None
        for c in pessoa._Pessoa__ContaBancarias:
            if c.NroConta == conta_numero:
                conta = c
                break
        if conta:
            pessoa._Pessoa__ContaBancarias.remove(conta)
            conta.banco.FecharConta(conta)
        else:
            print('Conta não encontrada.')

def realizar_saque(pessoas):
    pessoa = buscar_pessoa(pessoas)
    if pessoa:
        conta = buscar_conta(pessoa)
        if conta:
            valor = float(input('Valor do Saque: '))
            senha = input('Senha: ')
            if conta.VerificaSenha(senha):
                conta.saque(valor, senha)
            else:
                print(f'Senha incorreta.')

def realizar_deposito(pessoas):
    pessoa = buscar_pessoa(pessoas)
    if pessoa:
        conta = buscar_conta(pessoa)
        if conta:
            valor = float(input('Valor do Depósito: '))
            conta.deposito(valor)

def aplicar_novo_mes(pessoas):
    for pessoa in pessoas:
        for conta in pessoa._Pessoa__ContaBancarias:
            conta.NovoMes()

def buscar_pessoa(pessoas):
    cpf = input('Informe o CPF da pessoa: ')
    for pessoa in pessoas:
        if pessoa._Pessoa__cpf == cpf:
            return pessoa
    print('Pessoa não encontrada.')

def buscar_banco(bancos):
    numero_banco = int(input('Informe o número do banco: '))
    for banco in bancos:
        if banco._Banco__NroBanco == numero_banco:
            return banco
    print('Banco não encontrado.')


def buscar_conta(pessoa):
    conta_numero = int(input('Número da Conta: '))
    for conta in pessoa._Pessoa__ContaBancarias:
        if conta.NroConta == conta_numero:
            return conta
    print('Conta não encontrada.')

menu_principal()

