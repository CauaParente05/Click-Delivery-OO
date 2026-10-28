from modelos.avaliacao import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio

class Restaurante:
    restaurantes = []
    
    def __init__(self, nome: str = '', categoria: str = ''):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacoes = []
        self._cardapio = []
        Restaurante.restaurantes.append(self)
        
    
    def __str__(self):
        return f'{self._nome} | {self._categoria}'
    
    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome do Restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} | Status')
        for restaurante in cls.restaurantes:
            media = restaurante.media_avaliacoes
            avaliacao = media if media is not None else '-'
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(avaliacao).ljust(25)} | {restaurante.ativo}')
            
    @property
    def ativo(self):
        return '☑' if self._ativo else '☒'
    
    def alternar_estado(self):
        self._ativo = not self._ativo
    
    def avaliar(self, cliente, nota):
        if 0 <= nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacoes.append(avaliacao)
       
    @property 
    def media_avaliacoes(self):
        if not self._avaliacoes:
            return None
        
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacoes)
        quantidade_de_notas = len(self._avaliacoes)
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return 
    
    # def adicionar_bebida_no_cardapio(self, bebida):
    #     self._cardapio.append(bebida)
        
    # def adicionar_prato_no_cardapio(self, prato):
    #     self._cardapio.append(prato)
    
    def adicionar_no_cardapio(self, item):
        if isinstance(item, ItemCardapio):
            self._cardapio.append(item)
            
    @property
    def exibir_cardapio(self):
        print(f'Cardapio do Restaurante: {self._nome}:\n')
        for i,item in enumerate(self._cardapio, start=1):
            if hasattr(item, '_descricao'):
                mensagem_prato = f'{i}. Nome: {item._nome} | Preço: R$ {item._preco} | Descrição: {item._descricao}'
                print(mensagem_prato)
            elif hasattr(item, '_tamanho'):
                mensagem_bebida = f'{i}. Nome: {item._nome} | Preço: R$ {item._preco} | Tamanho: {item._tamanho} ml'
                print(mensagem_bebida)