class Cliente:
    def __init__(self, nome: str, cpf: str, telefone: str, endereco: str):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.endereco = endereco
        
c1 = Cliente('João', '123.456.789-10', '4002-8922', 'Rua ali de acola')
c2 = Cliente('Maria', '533.534.555-20', '9999-8752', 'Av. lá')
c3 = Cliente('Jacinto', '101.110.111-01', '1001-1100', 'Av. por ai')