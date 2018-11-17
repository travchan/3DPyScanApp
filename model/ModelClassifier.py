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
        self.generate_distribution_data(self.plyObject.vertices)

    def compare_models(self):
        pass

    def generate_distribution_data(self, vertices):
        distribution_data = []
        for b in range(1024):
            for i in range(1024 ^ 2):
                distribution_data.append(self._calc_length(vertices))
        return plt.hist(distribution_data, histtype='step', bins=40)

    def _calc_length(self, vertices):
        idx_1 = randint(0, len(vertices)-1)
        idx_2 = randint(0, len(vertices)-1)
        first_rand_vertex = vertices[idx_1]
        second_rand_vertex = vertices[idx_2]
        distance = self._get_euclidean_distance(first_rand_vertex, second_rand_vertex)

        return distance

    @staticmethod
    def _get_average(lst):
        return sum(lst) / len(lst)

    @staticmethod
    def _get_euclidean_distance(a, b):
        return np.linalg.norm(a - b)

    @staticmethod
    def _show_histogram():
        plt.title('Shape Distribution Graph')
        plt.ylabel('Frequency')
        plt.xlabel('Distance')
        plt.show()


if __name__ == "__main__":
    mesh = ModelClassifier('./scans/test_scans/Cube_Test01_BoxSize_Small(0).obj')
    mesh.classify()
