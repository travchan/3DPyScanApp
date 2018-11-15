import numpy as np
import trimesh as tmesh
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

    def classify(self):
        # plt.hist(self.plyObject.vertices)
        # plt.grid(True)
        # plt.show()
        print(self._calc_length())

    def _get_min_values(self):
        min_value = []
        for coordinates in self.plyObject.vertices:
            if len(min_value) == 0:
                min_value.extend(coordinates)
            if coordinates[0] <= min_value[0] and coordinates[2] <= min_value[2]:
                min_value = coordinates
        return min_value

    def _calc_length(self):
        vertices = self.plyObject.vertices
        starting_coords = self._get_min_values()
        total_y_arr = []

        for i in range(len(vertices) - 1):
            if vertices[i][1] == starting_coords[1] and vertices[i][2] == starting_coords[2]:

                total_y_arr.append(vertices[i][0])

        total_y = 0
        for i in range(len(total_y_arr) - 1):
            total_y += abs(total_y_arr[i] - total_y_arr[i + 1])

        return total_y

    @staticmethod
    def _get_average(lst):
        return sum(lst) / len(lst)


if __name__ == "__main__":
    mesh = ModelClassifier('./scans/test_scans/Cube_Test01_BoxSize_Small(0).obj')
    mesh.classify()
