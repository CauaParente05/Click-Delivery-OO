from modelos.cardapio.item_cardapio import ItemCardapio

class Bebida(ItemCardapio):
    def __init__(self, nome = '', preco = 0, tamanho = 0):
        super().__init__(nome, preco)
        self._tamanho = tamanho
        
    def __str__(self):
        return f'{super().__str__()} | Tamanho: {self._tamanho} ml'
    
    def aplicar_desconto(self):
            self._preco -= (self._preco * 0.05)