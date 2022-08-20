import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.backends.backend_qtagg import FigureCanvas


class Canvas(FigureCanvas):
    def __init__(self, graph, pos):
        self.fig, self.ax = plt.subplots(1, figsize=(10, 10))
        super().__init__(self.fig)
        self.plot = graph

        nx.draw_networkx_nodes(graph, pos, node_size=150)

        nx.draw_networkx_labels(graph, pos, font_size=7)

        nx.draw_networkx_edges(graph, pos, width=0.6)

        self.ax.axis('off')
        self.ax.plot()
        plt.close(self.fig)
