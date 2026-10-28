from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_teste = Restaurante('Teste', 'Qualquer')
bebida_teste = Bebida('B_teste', 5.50, 400)
prato_teste = Prato('P_teste', 24.90, 'Parmegiana de frango')
restaurante_teste.adicionar_no_cardapio(bebida_teste)
restaurante_teste.adicionar_no_cardapio(prato_teste)

def main():
    print(bebida_teste)
    print(prato_teste)
    restaurante_teste.exibir_cardapio
    pass

if __name__ == '__main__':
    main()