class ContaBancaria:
    def __init__(self, titular = '', saldo = 0.0):
        self._titular = titular.title()
        self._saldo = float(saldo)
        self._ativo = False
        
    def __str__(self):
        return f'Titular da conta: {self.titular} | Saldo: {self.saldo}'
    
    def ativar_conta(self):
        self._ativo = True
        
    @property
    def titular(self):
        return f'{self._titular}'
    
    @property
    def ativo(self):
        return '☑' if self._ativo else '☐'

    @property
    def saldo(self):
        return f'{self._saldo:.2f}'
    
c1 = ContaBancaria('Fulano', 1500.00)
c2 = ContaBancaria('Siclano', 400.00)
c3 = ContaBancaria('beltrano siclas', 950)

print(c3.titular)

class ClienteBanco:
    def __init__(self, nome = '', cpf = '', numero_da_conta = '', telefone = '', endereco = ''):
        self.nome = nome
        self.cpf = cpf
        self.numero_da_conta = numero_da_conta
        self.telefone = telefone
        self.endereco = endereco
        
    def mudar_endereco(self, novo_endereco = ''):
        self.endereco = novo_endereco
        
cb1 = ClienteBanco('Fulano', '123.456.789-10', '1', '4002-8922', 'Rua de lá')

print(cb1.endereco)

cb1.mudar_endereco('Rua de cá')

print(cb1.endereco)