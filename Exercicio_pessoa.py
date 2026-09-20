class Pessoa:
    def __init__(self, nome = '', idade = 0, profissao = ''):
        self._nome = nome
        self._idade = idade
        self._profissao = profissao
        
    def __str__(self):
        return f'Nome: {self._nome} | Idade: {self._idade} | Profissão: {self._profissao}'
    
    def aniversario(self):
        self._idade += 1
        
    @property
    def saudacao(self):
        if self._profissao:
            return f'Meu nome é {self._nome}, sou {self._profissao}'
        else:
            return f'Olá, sou {self._nome}!'
        
p1 = Pessoa('Fulano', 23, 'Desenvolvedor Back-End')

print(p1)

p1.aniversario()

print(p1.saudacao)

print(p1)

p2 = Pessoa('Siclano', 17)

print(p2.saudacao)