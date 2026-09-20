from modelos.restaurante import Restaurante

restaurante_forno_brasa = Restaurante('Forno & Brasa', 'Pizza')
restaurante_forno_brasa.avaliar('Cauã', 5)
restaurante_forno_brasa.avaliar('Fulano', 3.5)
restaurante_forno_brasa.avaliar('Siclano', 2.75)

restaurante_forno_brasa.alternar_estado()

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()