# clase que abarca los atributos y operaciones de un arbol
# creado el 30 de enero del 2013
# modificaciones 0
# revisiones 0

class Tree:
    def __init__(self,name):
        self.name = name
        self.nodes = []
        self.tag = ""
        self.text = ""
        self.title = ""
        self.desc = ""
    def setName(self,name):
        self.name = name
    def setTag(self,tag):
        self.tag = tag
    def setText(self,text):
        self.text = text
