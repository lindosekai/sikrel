# definicion de los atributos de un nodo y sus operaciones
# creado el 30 de enero del 2013
# modificaciones 0
# revisiones 0
class Node:
    def __init__(self,nodename):
        self.nodename = nodename
        self.tag = ""
        self.text = ""
        self.nodes = []
        self.type = "node"
    def addNode(self,node):
        self.nodes.append(node)
