from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_forno_brasa = Restaurante('Forno & Brasa', 'Pizza')
restaurante_sakura_gawa = Restaurante('Sakura Gawa', 'Japonesa')

restaurante_forno_brasa.alternar_estado()

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()