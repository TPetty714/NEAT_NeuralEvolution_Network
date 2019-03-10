import Node as n
import Connection as con
import random

class NEAT:
    def __init__(self, numInputs, numOutputs, genepool):
        self.genepool = genepool
        self.nodes = []
        self.connections = []
        for i in range(numInputs):
            node = n.Node(i, "input")
            self.nodes.append(node)
        for i in range(numOutputs):
            node = n.Node(999+i, "output")
            self.nodes.append(node)

    def createNode(self, w=None):
        if self.connections.__len__() == 0:
            return
        connection = self.connections[random.randint(0, self.connections.__len__()-1)]
        connection.active = False
        node = n.Node(self.nodes.__len__(), "hidden")
        self.mutateConnection(connection.inNode, node, 1)
        self.mutateConnection(node, connection.outNode, connection.w)
        self.nodes.append(node)
        temp = self.nodes[self.nodes.__len__()-2]
        self.nodes[self.nodes.__len__() - 2] = self.nodes[self.nodes.__len__()-1]
        self.nodes[self.nodes.__len__() - 1] = temp
        # print(str(self.nodes[self.nodes.__len__() - 2].num) + " " + str(self.nodes[self.nodes.__len__() - 1].num))

    def mutateConnection(self, inNode, outNode, w=None):
        key = str(inNode.num) + "to" + str(outNode.num)
        if key not in self.genepool.innovations:
            self.genepool.innovations[key] = self.genepool.innoNum
            self.genepool.innoNum += 1
        if w == None:
            connection = con.Connection(inNode, outNode, random.uniform(-2, 2), True, self.genepool.innovations[key])
        else:
            connection = con.Connection(inNode, outNode, w, True, self.genepool.innovations[key])
        inNode.outbound.append(connection)
        self.connections.append(connection)

    def createConnection(self):
        inNode = None
        outNode = None
        while inNode == None or outNode == None:
            inNode = self.nodes[random.randint(0,self.nodes.__len__()-1)]
            outNode = self.nodes[random.randint(0,self.nodes.__len__()-1)]
            if inNode == outNode:
                inNode = None
                outNode = None
                continue
            if inNode.type == "output":
                inNode = None
                continue
            if outNode.type == "input":
                outNode = None
                continue
            if inNode.num > outNode.num:
                temp = inNode
                inNode = outNode
                outNode = temp
            key = str(inNode.num) + "to" + str(outNode.num)
            if key not in self.genepool.innovations:
                self.genepool.innovations[key] = self.genepool.innoNum
                self.genepool.innoNum += 1
            connection = con.Connection(inNode, outNode, random.uniform(-2, 2), True, self.genepool.innovations[key])
            inNode.outbound.append(connection)
            self.connections.append(connection)


    def printNetwork(self):
        for i in range(self.nodes.__len__()):
            print(self.nodes[i].num)
        for i in range(self.connections.__len__()):
            connection = self.connections[i]
            print(str(connection.inNode.num) + " to " + str(connection.outNode.num) + " " + str(connection.innoNum))

    def testConnection(self):
        self.nodes[0].inputs.append(0)
        self.nodes[1].inputs.append(1)
        self.nodes[2].inputs.append(2)
        for node in self.nodes:
            print("Genome ", node.num)
            sum = 0
            for input in node.inputs:
                sum += input
            print("sum = ",sum)
            if node.type != "output":
                for connection in node.outbound:
                    print(str(connection.inNode.num) + " to " + str(connection.outNode.num) + " weight = " + str(connection.w) + " " + str(connection.active))
                    if connection.active:
                        connection.outNode.inputs.append(sum * connection.w)

