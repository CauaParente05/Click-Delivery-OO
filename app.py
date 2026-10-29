from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato
from modelos.cardapio.sobremesa import Sobremesa

restaurante_teste = Restaurante('Teste', 'Qualquer')
bebida_teste = Bebida('B_teste', 5.50, 400)
prato_teste = Prato('P_teste', 24.90, 'Parmegiana de frango')
restaurante_teste.adicionar_no_cardapio(bebida_teste)
restaurante_teste.adicionar_no_cardapio(prato_teste)
bebida_teste.aplicar_desconto()
prato_teste.aplicar_desconto()
teste = Sobremesa('S_teste', 12.50, 'Chocolate', 2, 'Musse de chocolate')

def main():
    restaurante_teste.exibir_cardapio
    pass

if __name__ == '__main__':
    main()