import sys

from PyQt5.QtWidgets import QApplication

from Canvas import Canvas
from Window import MainWindow, create
from utils import generate_cities, generate_population

if __name__ == '__main__':
    cities_list = generate_cities(cities_count=30, min_x=0, min_y=0, max_x=100, max_y=100)

    population = generate_population(cities=cities_list, population_size=200)

    best_route = sorted(population, key=lambda route: route.distance)[0]

    app = QApplication(sys.argv)
    window = MainWindow(population)
    window.show()
    pop, pos = create(population)
    window.pos = pos
    window.ui.verticalLayout_2.addWidget(Canvas(pop, pos))
    app.exec()
