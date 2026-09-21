from exercicio_veiculo.carro import Carro
from exercicio_veiculo.moto import Moto

# Carros
carro1 = Carro('Toyota', 'Corolla', 4)
carro2 = Carro('Volkswagen', 'Gol', 2)
carro3 = Carro('Honda', 'Civic', 4)

# Motos
moto1 = Moto('Honda', 'CG 160', 'Street')
moto2 = Moto('Yamaha', 'MT-03', 'Naked')
moto3 = Moto('Kawasaki', 'Ninja 400', 'Esportiva')

def main():
    print(moto1)
    print(moto2)
    print(moto3)
    print()
    print('-' * 65, '\n')
    print(carro1)
    print(carro2)
    print(carro3)
    
if __name__ == '__main__':
    main()