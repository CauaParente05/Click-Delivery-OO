from modelos.cardapio.item_cardapio import ItemCardapio

class Bebida(ItemCardapio):
    def __init__(self, nome = '', preco = 0, tamanho = 0):
        super().__init__(nome, preco)
        self._tamanho = tamanho