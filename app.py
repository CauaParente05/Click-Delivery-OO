from modelos.restaurante import Restaurante

restaurante_forno_brasa = Restaurante('Forno & Brasa', 'Pizza')
restaurante_forno_brasa.avaliar('Cauã', 10)
restaurante_forno_brasa.avaliar('Fulano', 7)
restaurante_forno_brasa.avaliar('Siclano', 5.5)

restaurante_forno_brasa.alternar_estado()

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()