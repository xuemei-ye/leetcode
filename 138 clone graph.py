

class Solution:

    def __init__(self):
        self.visited = {}

    def cloneGraph(self, node):

        if not node:
            return node

        if node in self.visited:
            return self.visited[node]

        cNode = Node(node, [])
        self.visited[node] = cNode

        if node.neighbors:
            cNode.neighbors = [self.cloneGraph(n) for n in node.neighbors]

        return cNode