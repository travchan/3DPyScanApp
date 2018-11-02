import numpy as np
import trimesh as tmesh

class ModelClassifier:
    """ Uses the trimesh and numpy libraries to extract .ply data for model classification
    """

    def __init__(self, model):
        """ Loads the .ply file for processing
        
        Arguments:
            model {file path} -- file path of the .ply file
        """

        self.plyObject = tmesh.load(model)

    def displayModel(self):
        """ placeholder function
        """

        self.plyObject.show()
    
    def classify(self):
        pass
    
if __name__ == "__main__":
    mesh = ModelClassifier('model/scans/Model.ply')
    mesh.displayModel()
