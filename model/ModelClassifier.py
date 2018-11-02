import numpy as np
import trimesh as tmesh

class ModelClassifier:

    def __init__(self, model):
        self.plyObject = tmesh.load('model/scans/Model.ply')

    def displayModel(self):
        self.plyObject.show()
    
if __name__ == "__main__":
    mesh = ModelClassifier('./Model.ply')
    mesh.displayModel()
