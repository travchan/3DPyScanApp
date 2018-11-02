import numpy as np
import trimesh as tmesh

class ModelClassifier:

    def __init__(self, model):
        self.plyObject = tmesh.load(model)

    def displayModel(self):
        self.plyObject.show()
    
if __name__ == "__main__":
    mesh = ModelClassifier('model/scans/Model.ply')
    mesh.displayModel()
