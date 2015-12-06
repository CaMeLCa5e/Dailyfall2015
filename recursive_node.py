class Node():
    def __init__(self, tree, data, parent=None):
        self.data = data
        self.parent = parent
        self.children = []
        self.tree = tree

    def find(self, x):
        if self.data is x: return self
        for node in self.children:
            n = node.find(x)
            if n: return n
        return None

n = Node(None, 1)
n.children = [Node(None, 2), Node(None, 3)]
print n.fine(3).data
