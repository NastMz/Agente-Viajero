import math

from dataclasses import dataclass


# Clase que representa una ciudad.
@dataclass(eq=True, frozen=True)
class City:
    name: str
    x: int
    y: int

    # Método para calcular la distancia entre dos ciudades
    def get_distance(self, to_city):
        xx = to_city.x - self.x
        yy = to_city.y - self.y

        return math.sqrt(math.pow(xx, 2) + math.pow(yy, 2))
