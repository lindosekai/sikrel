from Sikrel import Sikrel

skrl = Sikrel()

def init():
    VERSION = "v0.0.1"
    print "+---------------------------------------------------------+"
    print "|         Wellcome to SIKREL Console  {}              |".format(VERSION)
    print "+---------------------------------------------------------+"
    print
    print
def prompt():
    pr = ""
    command = raw_input("command >> ")
    return command
def helpme():
    print
    print ">> Wellcome to SIKREL help section v0.0.1"
    print ">> Esta es la ayuda del Lenguaje Simple de Representacion de conocimientos"
    print ">> En esta version hay muy pocas funciones, pero esta es la introduccion al sistema"
    print ">> para iniciar debes usar el comando load {archivo.kre} donde el archivo.kre es un archivo de conocimientos creado con el lenguaje SIKREL"
    print
def parse(command):
    divs = command.split(' ')
    if len(divs)==1:
        if divs[0]=="help":
            helpme()
        elif divs[0]=="viewlists":
            skrl.viewLists()
        elif divs[0]=="viewdefs":
            skrl.viewDefs()
        elif divs[0]=="viewobjs":
            skrl.viewObjs()
        elif divs[0]=="info":
            skrl.info()
        elif divs[0]=="viewtrees":
            skrl.viewTrees()
        elif divs[0]=="clean":
            skrl.clean()
        else:
            print "[-] Command '{0}' not Found".format(divs[0])
    else:
        if divs[0]=="load":
            skrl.load(divs[1])
        elif divs[0]=="listar":
            skrl.viewList(divs[1])
        elif divs[0]=="whatis":
            skrl.viewDef(divs[1])
        elif divs[0]=="viewobj":
            skrl.viewObj(divs[1].split('\n')[0])
        elif divs[0]=="viewtree":
            skrl.viewTree(divs[1].split('\n')[0])
        elif divs[0]=="treeme":
            skrl.TreeMe(divs[1].split('\n')[0])

init()
while True:
    cx = prompt()
    if cx=="exit":
        exit(0)
    else:
        parse(cx)

print "Bye!"
