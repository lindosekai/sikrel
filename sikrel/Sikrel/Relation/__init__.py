# modulo experimental Relation
# define relaciones entre objetos un los objetos tendran
# 0 o mas relaciones definidad en esta clase
# experimental 31 de enero del 2013

class Relation:
    def __init__(self):
        self.type = ""
        self.obj = object()
    def isBrother(self,obj):
        self.type = "brother"
        self.obj = obj
