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
            print(f'{musica.nome} | {musica.artista} | {musica.duracao:.2f}')
            
musica1 = Musica(nome='Under Pressure', artista='Queen & David Bowie', duracao=2.48)
musica2 = Musica(nome='The Trooper', artista='Iron Maiden', duracao=2.45)
musica3 = Musica(nome='Hotel California', artista='Eagles', duracao=3.90)      

Musica.listar_musicas()