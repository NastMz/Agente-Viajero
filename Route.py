# Clase que representa una ruta.
# Esta clase será nuestro "cromosoma"
class Route:
    def __init__(self, cities_list):
        self.cities = cities_list  # Lista de ciudades de la ruta
        self.distance = 0  # Distancia total de la ruta
        for i in range(len(self.cities) - 1):  # Calculo de la distancia total de la ruta
            self.distance += self.cities[i].get_distance(self.cities[i + 1])

