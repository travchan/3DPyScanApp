import numpy as np
import trimesh as tmesh
from random import choice
import matplotlib.pyplot as plt
import os


class ModelClassifier:
    """ Uses the trimesh and matplotlib libraries to extract data for model classification
    """

    def __init__(self, model):
        """ Loads the .ply file for processing
        
        Arguments:
            model {file path} -- file path of the .ply file
        """

        self.plyObject = tmesh.load(model)
        self.distribution_data = []

    def classify(self):
        #  TODO: Add model Scaling
        #  TODO: Add averages from multiple cube files for comparison
        #  TODO: Documentation
        hist_data = self.generate_distribution_data(self.plyObject.vertices)
        results = self.compare_models(hist_data)

        if results[0] is True and results[1] is True:
            print("It is a Cube!")
        else:
            print("It is not a cube")

    def compare_models(self, hist_data):
        occurrences = list(hist_data[0])
        distances = list(hist_data[1])

        shape_data = self._get_shape_data()
        o_data = shape_data[1].strip("[").strip("]").split(",")
        o_data = [float(i) for i in o_data]
        d_data = shape_data[2].strip("[").strip("]").split(",")
        d_data = [float(i) for i in d_data]

        result1 = self.data_check(occurrences, o_data)
        result2 = self.data_check(distances, d_data)

        return result1, result2

    def generate_distribution_data(self, vertices):
        distribution_data = []
        for b in range(1024):
            for i in range(1024 ^ 2):
                distribution_data.append(self._calc_length(vertices))
        return plt.hist(distribution_data, histtype='step', bins=40)

    def _calc_length(self, vertices):
        used_coordinate_pairs = []
        first_rand_vertex = choice(vertices)
        second_rand_vertex = choice(vertices)

        while True:
            if set(first_rand_vertex).intersection(second_rand_vertex) != 3:
                if [first_rand_vertex, second_rand_vertex] not in used_coordinate_pairs:
                    used_coordinate_pairs.append([first_rand_vertex, second_rand_vertex])
                    break
                else:
                    first_rand_vertex = choice(vertices)
                    second_rand_vertex = choice(vertices)
            else:
                first_rand_vertex = choice(vertices)
                second_rand_vertex = choice(vertices)

        distance = self._get_euclidean_distance(first_rand_vertex, second_rand_vertex)

        return distance

    @staticmethod
    def _get_average(lst):
        return sum(lst) / len(lst)

    @staticmethod
    def _get_euclidean_distance(a, b):
        return np.linalg.norm(a - b)

    @staticmethod
    def _get_shape_data():
        with open(os.path.join(os.path.dirname(__file__), "training_data.txt"), 'r') as data:
            lines = data.readlines()
            return lines[0].split(";")

    @staticmethod
    def data_check(data1, data2):
        checks_passed = 0
        for index in range(len(data1)):
            lower_bound = data2[index] - data2[index] * 0.20
            upper_bound = data2[index] + data2[index] * 0.20
            if upper_bound >= data1[index] >= lower_bound:
                checks_passed += 1
        if checks_passed >= len(data1)*0.75:
            return True
        else:
            return False

    @staticmethod
    def _show_histogram():
        plt.title('Shape Distribution Graph')
        plt.ylabel('Frequency')
        plt.xlabel('Distance')
        plt.show()


if __name__ == "__main__":
    mesh = ModelClassifier('./scans/test_scans/Cube_Test01_BoxSize_Small(0).obj')
    mesh.classify()
