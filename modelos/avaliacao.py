class Avaliacao:
    def __init__(self, cliente = '', nota = 0.0):
        self._cliente = cliente.title()
        self._nota = float(nota)