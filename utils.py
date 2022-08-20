import csv
import random
from copy import deepcopy

from City import City
from Route import Route


# Función para obtener un conjunto de ciudades al azar del archivo para utilizar en el algoritmo
# cities_count = Número de ciudades que se van a generar
# min_x, min_y = Minima distancia que puede haber en las coordenadas (x, y) hasta esa ciudad
# max_x, max_y = Máxima distancia que puede haber en las coordenadas (x, y) hasta esa ciudad
def generate_cities(cities_count, min_x, min_y, max_x, max_y):
    cities = set()
    with open("cities.csv", encoding="utf-8") as file:
        data = csv.reader(file)
        for city in data:
            x = random.randint(min_x, max_x)
            y = random.randint(min_y, max_y)
            cities.add(City(name=city[0], x=x, y=y))

    return set(random.sample(cities, cities_count))


# Función para generar la población inicial que utilizara el algoritmo
# cities = Conjunto de ciudades que va a utilizar el algoritmo
# population_size = Tamaño de la población inicial
def generate_population(cities, population_size):
    population = []
    for _ in range(population_size):
        population.append(
            Route(random.sample(cities, len(cities)))
        )
    return population


# Función para seleccionar a los que serán los padres
# population = Población en la cual se seleccionarán los padres
# number_parents = Número de padres que se seleccionarán de la población
def select_parents(population, number_parents):
    sort_by_distance_population = sorted(population, key=lambda route: route.distance)
    return sort_by_distance_population[:number_parents]


# Función para cruzar a los padres y obtener una nueva población de hijos
# parents = Conjunto de padres que se van a cruzar
# population_size = Tamaño de la nueva población conformada por los hijos y los padres
def crossover(parents, population_size):
    number_children = population_size - len(parents)  # Número de hijos que debe de haber para completar la población

    new_children = []
    for _ in range(number_children):  # Obtener dos padres al azar para cada hijo
        parent1, parent2 = random.sample(parents, 2)
        new_child = Route(_cross_parents(parent1.cities, parent2.cities))
        new_children.append(new_child)

    return new_children


# Función que implementa el algoritmo de cruce para obtener un hijo
def _cross_parents(parent1, parent2):
    child = deepcopy(parent2)

    for index_parent1, value_parent1 in enumerate(parent1):
        index_parent2 = child.index(value_parent1)
        child[index_parent2] = child[index_parent1]
        child[index_parent1] = value_parent1

    return child


# Función para realizar mutaciones a los hijos
def mutate(children):
    mutated_children = []

    for child in children:
        cities = deepcopy(child.cities)

        if 0.7 > random.random():
            swap_from = random.randint(0, len(cities) - 1)
            swap_to = random.randint(0, len(cities) - 1)
            while swap_to == swap_from:
                swap_to = random.randint(0, len(cities) - 1)

            aux = cities[swap_to]
            cities[swap_to] = cities[swap_from]
            cities[swap_from] = aux

        mutated_children.append(Route(cities))

    return mutated_children


