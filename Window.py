import networkx as nx
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QMainWindow

from Canvas import Canvas
from ui_interface import Ui_MainWindow
from utils import select_parents, crossover, mutate


def create(population):
    graph = nx.DiGraph()
    nodes = []
    edges = []
    best_route = sorted(population, key=lambda route: route.distance)[0]
    for index in range(len(best_route.cities) - 1):
        nodes.append(best_route.cities[index].name)
        edges.append((best_route.cities[index].name, best_route.cities[index + 1].name))

    graph.add_nodes_from(nodes)
    graph.add_edges_from(edges)

    pos = nx.spring_layout(graph, k=8)

    return graph, pos


class MainWindow(QMainWindow):
    def __init__(self, population):
        super().__init__()
        self.dragPos = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.population = population
        self.generation = 0
        self.pos = None

        best_route = sorted(self.population, key=lambda route: route.distance)[0]
        self.ui.label_4.setText(str(f'{best_route.distance:.3f}'))

        self.ui.pushButton_2.setEnabled(False)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update)

        self.ui.startBtn.clicked.connect(lambda: self.start_timer())
        self.ui.pushButton_2.clicked.connect(lambda: self.stop_timer())

    def start_timer(self):
        self.timer.start(800)
        self.ui.startBtn.setEnabled(False)
        self.ui.pushButton_2.setEnabled(True)

    def stop_timer(self):
        self.timer.stop()
        self.ui.pushButton_2.setEnabled(False)
        self.ui.startBtn.setEnabled(True)

    def update(self):
        selected_parents = select_parents(population=self.population, number_parents=10)

        new_children = crossover(parents=selected_parents, population_size=200)

        mutated_children = mutate(children=new_children)

        self.population = selected_parents + mutated_children

        self.generation += 1

        best_route = sorted(self.population, key=lambda route: route.distance)[0]

        self.ui.label.setText(str(self.generation))
        self.ui.label_4.setText(str(f'{best_route.distance:.3f}'))
        pop, p = create(self.population)
        self.ui.verticalLayout_2.replaceWidget(self.ui.verticalLayout_2.itemAt(0).widget(),
                                               Canvas(pop, self.pos))
