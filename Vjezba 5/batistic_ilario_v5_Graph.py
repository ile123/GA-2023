class Graph:
    def __init__(self, vertices, edges, labels, arcs, matrices) -> None:
        self.vertices = vertices
        self.edges = edges
        self.labels = labels
        self.arcs = arcs
        self.matrices = matrices
    
    def __str__(self) -> str:
        return f'\nVertices: {self.vertices}\nEdges: {self.edges}\nLabels: {self.labels}\nArcs: {self.arcs}\nMatrices: {self.matrices}'