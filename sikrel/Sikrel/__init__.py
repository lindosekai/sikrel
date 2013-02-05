# clase principal de SIKREL
# parser principal del sistema y cargador en memoria de los datos
from Object import Object
from Tree import Tree
from Node import Node 
class Sikrel:
    def __init__(self):
        self.lists = []
        self.definitions = []
        self.objects = {}
        self.trees = {}
        self.kre_name = ""
    def load(self,filename):
        if(self.kre_name==filename):
            print "[-] El Modulo Requerido ya esta Cargado"
        else:
            print " [+] loadding {0}...".format(filename)
            self.kre_name = filename
            self.lists = []
            self.definitions = []
            self.objetcs = {}
            self.trees = {}
            nodes = {}
            nodelist = []
            f = open("{0}.kre".format(filename))
            for l in f.readlines():
                toks = l.split(' ')
                if toks[0]=="list":
                    objs = toks[1].split(":")
                    listname = objs[0]
                    listay = list()
                    listaz = list()
                    elements = objs[1].split(',')
                    for el in elements:
                        listay.append(el)
                    listaz.append(listname)
                    listaz.append(listay)
                    self.lists.append(listaz)
                elif toks[0]=="define":
                    part1 = l.split(":")
                    part2 = part1[0].split(' ')
                    defname = part2[1]
                    listax = list()
                    listax.append(defname)
                    listax.append(part1[1])
                    self.definitions.append(listax)
                elif toks[0]=="object":
                    self.objects[toks[1].split('\n')[0]] = Object()
                elif toks[0]=="tree":
# en esta seccion se cargan los nombres de los arboles en memoria
                    self.trees[toks[1].split('\n')[0]]=Tree(toks[1].split('\n')[0])
                elif toks[0]=="node":
                    # en esta parte temporal se guardan los nodos espeficifados para luego ordenarlos en los
                    # arboles correspondientes
                    nodes[toks[1].split('\n')[0]] = Node(toks[1].split('\n')[0])
                else:
                    for obj in self.objects:
                        #print obj
                        if len(toks)==3:
                            if toks[0] == obj:
                                if toks[1] == "color":
                                     self.objects[toks[0].split('\n')[0]].color = toks[2].split('\n')[0]
                                elif toks[1]=="form":
                                     self.objects[toks[0].split('\n')[0]].form = toks[2].split('\n')[0]
                    st = l.split(":")
                    co = st[0].split(" ")
                    for t in self.trees:
                        if co[0]==self.trees[t].name:
                            if co[1]=="desc":
                                self.trees[t].desc = st[1]
                            elif co[1]=="title":
                                self.trees[t].title = st[1]
                    for n in nodes:
                        if toks[0]==n:
#                            print n, co[1], st[1].split("\n")[0]
                            if co[1]=="tag":
                                nodes[n].tag = st[1].split("\n")[0]
                            elif co[1]=="txt":
                                nodes[n].text = st[1].split("\n")[0]
                            if co[1]=="addnode":
                                parent = nodes[n]
                                son = nodes[st[1].split("\n")[0]]
                                #print "adding {0}->{1}".format(son.nodename,parent.nodename)
                    #hacemos una verificacion
                    for t in self.trees:
                        if t ==toks[0]:
                            if len(co)==2 and co[1]=="addnode":
#co1 addnode
#co[0] tree master
#st[1] node of the tree
#                             print "{0}--{1}--{2}".format(co[0],co[1],st[1])
                             self.trees[t].nodes.append(nodes[st[1].split("\n")[0]])

        self.info()
        return True
    def viewLists(self):
        if self.kre_name!="":
            print " [+] Mostrando Listas del Archivo {0}.kre".format(self.kre_name)
            for l in self.lists:
                lx = l
                print "    - {0}".format(lx[0])
        else : print " [-] No has cargado ningun archivo de Conocimiento"
    def viewDefs(self):
        if self.kre_name!="":
            print " [+] Mostrando Definiciones del Archivo {0}.kre".format(self.kre_name)
            for d in self.definitions:
                print "    - {0}".format(d[0])
        else : print " [-] No has cargado ningun archivo de Conocimiento"
    def viewList(self,list_name):
        v = list()
        f = False
        for l in self.lists:
            lx = l
            if(lx[0]==list_name):
                v = lx[1]
                f = True
                break
        if f==True:
            for x in v:
                print "    -{0}".format(x)
            print " [+] Total de Elementos : {0}".format(len(v))
        else :
            print " [-] la lista '{0}' no existe en el archivo de Conocimiento actual".format(list_name)
        return self.lists
    def viewDef(self,concept):
        for d in self.definitions:
            if d[0]==concept:
                print "{0} : {1}".format(concept,d[1])
                break
    def viewObjs(self):
        print self.objects
    def viewObj(self,obj):
        print "[+] color : {0}".format(self.objects[obj].color)
        print "[+] forma : {0}".format(self.objects[obj].form)
    def info(self):
        if self.kre_name!="":
            print "  [+] Cargado el Modulo {0}".format(self.kre_name)
            if len(self.lists)>0:
                print "  [+] Numero de Listas {0}".format(len(self.lists))
            if len(self.definitions)>0:
                print "  [+] Numero de Definiciones {0}".format(len(self.definitions))
            if len(self.objects)>0:
                print "  [+] Numero de objectos {0}".format(len(self.objects))
            if len(self.trees)>0:
                print "  [+] Numero de Arboles {0}".format(len(self.trees))
        else :
            print "  [-] no hay ningun Documento de Conocimiento cargado"
            print "  [-] Utilize \"load documento.kre\""
    def clean(self):
        if self.kre_name !="":
            self.kre_name = ""
            print "  [+] Limpiando Listas"
            self.lists = []
            print "  [+] Limpiando Definiciones"
            self.definitions = []
            print "  [+] limpiando Objetos"
            self.objects = {}
        else:
            print "  [-] No hay ningun kre-documento cargado"
    def viewTrees(self):
        for t in self.trees:
            print "    - {0}".format(self.trees[t].name)
    def viewTree(self,treename):
        print "   -desc  : {0}".format(self.trees[treename].desc.split("\n")[0])
        print "   -title : {0}".format(self.trees[treename].title.split("\n")[0])
    def TreeMe(self,treename):
        m = self.trees[treename]
        for n in m.nodes:
            while True:
                print n
                c = n.nodes
                if len(c)>0:
                    for x in n.nodes:
                         print x
                else :
                    break
                
