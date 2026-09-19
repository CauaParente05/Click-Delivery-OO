class Musica:
    musicas = []
    
    def __init__(self, nome, artista, duracao: float):
        self.nome = nome
        self.artista = artista
        self.duracao = duracao
        Musica.musicas.append(self)
    def __str__(self):
        print(f'{self.nome} | {self.artista}')
        
    def listar_musicas():
        for musica in Musica.musicas:
            print(f'{musica.nome} | {musica.artista} | {musica.duracao}')
            
m1 = Musica('Shape of You', 'Ed. Sheeran', 3.43)        

Musica.listar_musicas()