

class node():
    def __init__(self, nodeID,CHF,ram,maxexe,ExecutionTime):
        self.nodeID = nodeID
        self.CHF = CHF
        self.ram = ram
        #self.cpu = cpu
        #self.storage =storage
        self.maxexe = maxexe
        self.ExecutionTime = ExecutionTime
        self.totalresource=int(ram) #int(storage) + int (cpu)


def toporeader():
    file1 = 'Topology/topo'
    Fopen = open(file1,'r')
    nodedict ={}
    for line in Fopen:
        nodeID = int(line.split()[0])
        ram = int(line.split()[1])
        #cpu = line.split()[2]
        #storage = line.split()[3]
        chf = line.split()[-1]
        ExeTime = Exectio(chf)
        maxexe = maxset(chf)
        nodeOBJ = node(nodeID,chf,ram,maxexe,ExeTime) #chf and ram to process chf
        nodedict[nodeID]=nodeOBJ
    print nodedict
    return nodedict

def Exectio(chf):
    if float(chf) <= 0.1:
        return 15
    elif float(chf) > 0.2 and float(chf) <= 0.5:
        return 10
    elif float(chf) > 0.5 and float(chf) <= 0.7:
        return 5
    elif float(chf) > 1.0:
        return 5


def maxset(chf):
    if float(chf) <= 0.1:
        return 3
    elif float(chf) > 0.2 and float(chf) <= 0.5:
        return 10
    elif float(chf) > 0.5 and float(chf) <= 0.7:
        return 10
    elif float(chf) > 1.0:
        return 10




