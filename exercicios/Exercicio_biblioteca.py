from exercicios.Exercicio_livro import Livro

l1 = Livro('O Hobbit', 'J.R.R. Tolkien', 1937)

l1.emprestar()

print(l1._disponivel)

Livro.verificar_disponibilidade(1937)