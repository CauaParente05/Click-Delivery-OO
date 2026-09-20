class Livro:
    livros = []
    
    def __init__(self, titulo, autor, ano_publicacao):
        self._titulo = titulo
        self._autor = autor
        self._ano_publicacao = ano_publicacao
        self._disponivel = True
        Livro.livros.append(self)
        
    def __str__(self):
        return f'{self._titulo} | Autor: {self._autor} | Ano de Publicacao: {self._ano_publicacao}'
    
    def emprestar(self):
        self._disponivel = False
        
    @staticmethod
    def verificar_disponibilidade(ano):
        livros_disponiveis = [livro for livro in Livro.livros if ano == livro._ano_publicacao and livro._disponivel]
        return livros_disponiveis
    
l1 = Livro('Dom Casmurro', 'Machado de Assis', 1899)
l2 = Livro('1984', 'George Orwell', 1949)

for livro in Livro.verificar_disponibilidade(1949):
    print(livro)