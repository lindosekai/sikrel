import sys

args = sys.argv

if(len(args)<2):
    print "uso : "
    print "\t{0} filename.kre".format(args[0])
else :
    param = args[1]
    if param=="--help":
        print "Ayuda"
    else:
        f = open(param)
        for l in f.readlines():
            toks = l.split(' ')
            if toks[0]=="list":
                objs = toks[1].split(":")
                listname = objs[0]
                elements = objs[1].split(',')
                print "[+] ",listname
                for el in elements:
                    print "\t",el

