class Connection:
    inNode = None
    outNode = None
    w = 0
    active = False
    innoNum = 0

    def __init__(self, inNode, outNode, w, active, innoNum):
        self.inNode = inNode
        self.outNode = outNode
        self.w = w
        self.active = active
        self.innoNum = innoNum