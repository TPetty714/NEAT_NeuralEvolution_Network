class Node:
    def __init__(self, num, type):
        self.num = num
        self.type = type
        self.inputs = []
        self.outbound = []

    def addInput(self, val):
        self.inputs.append(val)
