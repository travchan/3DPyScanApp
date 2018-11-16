import numpy as np
import trimesh as tmesh
from random import randint
import matplotlib.pyplot as plt


class ModelClassifier:
    """ Uses the trimesh and numpy libraries to extract .ply data for model classification
    """

    def __init__(self, model):
        """ Loads the .ply file for processing
        
        Arguments:
            model {file path} -- file path of the .ply file
        """

        self.plyObject = tmesh.load(model)
        self.distribution_data = []

    def classify(self):
        self.generate_dist_graph_data()
        plt.hist(self.distribution_data)
        plt.grid(True)
        plt.show()

    def _calc_length(self):
        vertices = self.plyObject.vertices
        idx_1 = randint(0, len(vertices)-1)
        idx_2 = randint(0, len(vertices)-1)
        first_rand_vertice = vertices[idx_1]
        second_rand_vertice = vertices[idx_2]
        distance = self._get_euclidean_distance(first_rand_vertice, second_rand_vertice)

        return distance

    def generate_dist_graph_data(self):
        for i in range(1024^2):
            self.distribution_data.append(self._calc_length())

    @staticmethod
    def _get_average(lst):
        return sum(lst) / len(lst)

    @staticmethod
    def _get_euclidean_distance(a, b):
        return np.linalg.norm(a - b)


if __name__ == "__main__":
    mesh = ModelClassifier('./scans/test_scans/Cube_Test01_BoxSize_Small(0).obj')
    mesh.classify()
