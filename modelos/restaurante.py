from modelos.avaliacao import Avaliacao

class Restaurante:
    restaurantes = []
    
    def __init__(self, nome: str = '', categoria: str = ''):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacoes = []
        Restaurante.restaurantes.append(self)
    
    def __str__(self):
        return f'{self._nome} | {self._categoria}'
    
    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome do Restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} | Status')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante.ativo}')
            
    @property
    def ativo(self):
        return '☑' if self._ativo else '☒'
    
    def alternar_estado(self):
        self._ativo = not self._ativo
    
    def avaliar(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacoes.append(avaliacao)
       
    @property 
    def media_avaliacoes(self):
        if not self._avaliacoes:
            return 0
        
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacoes)
        quatidade_de_notas = len(self._avaliacoes)
        media = round(soma_das_notas / quatidade_de_notas, 1)
        return media