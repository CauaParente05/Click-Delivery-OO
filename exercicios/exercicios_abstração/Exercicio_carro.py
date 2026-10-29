from exercicios.exercicios_abstração.Exercicio_veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, marca, modelo, cor):
        super().__init__(marca, modelo)
        self._cor = cor
        
    def ligar(self):
        return f'Carro ligado'