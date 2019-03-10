import Genepool as gp

def main():
    genepool = gp.Genepool(5, 3, 1)
    genepool.mutate()
    genepool.testNetwork()

if __name__ == '__main__':
    main()