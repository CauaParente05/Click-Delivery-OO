class Restaurante:
    def __init__(self, nome: str, categoria: str, dono: str):
        self.nome = nome
        self. categoria = categoria
        self.ativo = False
        self.aberto = False
        self.dono = dono
    
    def __str__(self):
        return f'{self.nome} | {self.categoria} | {self.dono}'
    
r1 = Restaurante('Restaurante só Regionais', 'Regional', 'Cauã Parente')

print(r1)