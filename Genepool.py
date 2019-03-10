import NEAT as nw

class Genepool:
    innoNum = 1
    innovations = {}
    genomes = []

    def __init__(self, numGenomes, inputs, outputs):
        for i in range(numGenomes):
            print("Creating genome", i)
            self.genomes.append(nw.NEAT(inputs, outputs, self))
            # self.genomes[i].printNetwork()

    def mutate(self):
        i = 1
        for genome in self.genomes:
            # print("Genome " + str(i))
            # genome.createNode()
            genome.createConnection()
            genome.createNode()
            # genome.printNetwork()
            # i+=1

    def testNetwork(self):
        i = 1
        for genome in self.genomes:
            print("Network " + str(i))
            genome.testConnection()
            i+=1