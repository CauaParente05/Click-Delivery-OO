class ItemCardapio:
    def __init__(self, nome: str = '', preco: float = 0.0):
        self._nome = nome
        self._preco = float(preco)
        
    def __str__(self):
        return f'Item: {self._nome} | Preço: {self.preco}'
    
    @property
    def preco(self):
        return f'{self._preco:.2f}'