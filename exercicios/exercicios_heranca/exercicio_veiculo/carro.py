from .veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, marca, modelo, qtd_portas):
        super().__init__(marca, modelo)
        self.qtd_portas = qtd_portas
        
    def __str__(self):
        return f'{super().__str__()} | Portas: {self.qtd_portas}'