import queue


class Graph:

    def __init__(self, n):
        self.nVertices = n
        self.adjMat = [[0 for i in range(self.nVertices)]
                       for j in range(self.nVertices)]

    def addEdge(self, v1, v2):
        if self.adjMat[v1][v2] == 1:
            print("Edge already exists !!!")
            return
        self.adjMat[v1][v2] = 1
        self.adjMat[v2][v1] = 1

    def edgeExists(self, v1, v2):
        return self.adjMat[v1][v2] == 1

    def removeEdge(self, v1, v2):
        if self.edgeExists(v1, v2):
            self.adjMat[v1][v2] = 0
            self.adjMat[v2][v1] = 0
            return

    def __str__(self):
        return (str(self.adjMat))

    # --------------- BFS Traversal for connected or disconnected components ----------------
    def fullBFSTraversal(self, sv=0):

        nodes_visited = [0 for i in range(self.nVertices)]
        componentNo = 0

        for i in range(self.nVertices):
            if nodes_visited[i] == 0:
                componentNo += 1
                print(f"\nFor component : {componentNo}\n")
                nodes_visited = self.BFSTraversal(sv=i, visited=nodes_visited)

    # ---------------- core BFS traversal code -------------------------------

    def BFSTraversal(self, sv=0, visited=[], printnode=True):

        if visited == []:
            visited = [0 for i in range(self.nVertices)]

        q = queue.Queue()

        q.put(sv)
        visited[sv] = 1

        while q.empty() != True:

            poppedNode = q.get()
            if printnode == True:
                print(f"\tNode visited : {poppedNode}")
            for nodeNo in range(self.nVertices):
                if self.adjMat[poppedNode][nodeNo] == 1 and visited[nodeNo] != 1:
                    q.put(nodeNo)
                    visited[nodeNo] = 1

        return visited

    # --------------- connectectivity check of graph using BFS ------------------------
    def isConnectedBFS(self, printnode=False):

        visited = self.BFSTraversal(printnode=False)
        for i in range(len(visited)):
            if visited[i] == 0:
                print("The Graph is not connected !!!")
                break
        else:
            print("The graph is connected !!!")
        return

    # ---------------  connectectivity check between nodes using BFS   ------------------------

    def hasPathBFSTraversal(self, v1, v2):

        visited = [0 for i in range(self.nVertices)]

        q = queue.Queue()

        q.put(v1)
        visited[v1] = 1

        while q.empty() != True:

            poppedNode = q.get()
            for nodeNo in range(self.nVertices):
                if self.adjMat[poppedNode][nodeNo] == 1 and visited[nodeNo] != 1:
                    if nodeNo == v2:
                        print(f"Node {v1} has a path to node {v2}")
                        return True
                    q.put(nodeNo)
                    visited[nodeNo] = 1
        print(f"Node {v1} has No PATH to node {v2}")
        return False

    # --------------- print path using the BFS Traversal -----------------------------
    def printPathBFS(self, v1, v2):

        if v1 == v2:
            return [v1]

        visited = [0 for i in range(self.nVertices)]
        parent = [-1 for i in range(self.nVertices)]

        q = queue.Queue()

        q.put(v1)
        visited[v1] = 1
        parent[v1] = v1

        path = []

        while q.empty() != True:

            poppedNode = q.get()
            for nodeNo in range(self.nVertices):
                if self.adjMat[poppedNode][nodeNo] == 1 and visited[nodeNo] != 1:

                    '''parent must be added early as if dest reached 
                    then parent will help traverse the full path to source else it will be -1 only'''

                    parent[nodeNo] = poppedNode

                    if nodeNo == v2:
                        temp = v2
                        path.append(temp)
                        while parent[temp] != temp:
                            temp = parent[temp]
                            path.append(temp)
                        print(
                            f"The shortest path from {v1} to {v2} : ", end=' ')
                        print(path)
                        return

                    q.put(nodeNo)
                    visited[nodeNo] = 1

        if len(path) == 0:
            print(f"There is no path from {v1} to {v2}")
            return

    # ---------------- define the dfs helper function --------------

    def dfshelper(self, visited, sv=0, printnode=True):

        if visited[sv] == 1:
            return visited

        if printnode == True:
            print(f"{sv}", end=" ")
        visited[sv] = 1

        for i in range(self.nVertices):
            if self.adjMat[sv][i] == 1 and visited[i] != 1:
                visited = self.dfshelper(visited, i, printnode)

        return visited

    # ---------------------------------- the core DFS function --------------
    def DFStraversal(self, visited=None, sv=0, printnode=True):
        if visited == None:
            visited = [0 for i in range(self.nVertices)]
        visited = self.dfshelper(visited, sv, printnode)
        return visited

    # ------------------ DFS Traversal for connected or disconnected Graphs----------------
    def fullDFStraversal(self):

        visited = [0 for i in range(self.nVertices)]
        componentNo = 0
        for i in range(self.nVertices):
            if visited[i] != 1:
                componentNo += 1
                print(f"\nFor Component : {componentNo} \n")
                visited = self.DFStraversal(visited, sv=i)
                print()

    # ----------------  connectectivity check of graph using BFS ------------------------
    def isConnectedDFS(self, printnode=False):

        visited = self.DFStraversal(sv=0, printnode=printnode)
        for i in range(len(visited)):
            if visited[i] == 0:
                print("The Graph is not connected !!!")
                break
        else:
            print("The graph is connected !!!")
        return

    # ------------------------   connectectivity check between nodes using DFS   ------------------------

    def hasPathDFSTraversalhelper(self, visited, v1, v2):

        if self.adjMat[v1][v2] == 1:
            return True

        connected = False
        visited[v1] = 1

        for i in range(self.nVertices):
            if self.adjMat[v1][i] == 1 and visited[i] != 1:
                connected = self.hasPathDFSTraversalhelper(visited, i, v2)
                if connected:
                    break

        return connected

    def hasPathDFSTraversal(self, v1, v2):

        visited = [0 for i in range(self.nVertices)]

        connected = self.hasPathDFSTraversalhelper(visited, v1, v2)

        if connected:
            print(f"\nNodes {v1} and {v2} are connected !!!")
        else:
            print(f"\nNodes {v1} and {v2} are not connected !!!")
        return

    # -------------------- print path using the DFS Traversal -----------------------------

    def printPathDFShelper(self, v1, v2, visited):

        if self.adjMat[v1][v2] == 1:
            return [v2, v1]

        path = []
        visited[v1] = 1

        for i in range(self.nVertices):
            if self.adjMat[v1][i] == 1 and visited[i] != 1:
                path = self.printPathDFShelper(i, v2, visited)
                if path != []:
                    path.append(v1)
                    break
        return path

    def printPathDFS(self, v1, v2):
        visited = [0 for i in range(self.nVertices)]
        path = self.printPathDFShelper(v1, v2, visited)

        if path != []:
            print(f"\nThe path between nodes {v1} and {v2} is : ", path)
        else:
            print(
                f"\nThere is No path between nodes {v1} and {v2}. They are disconnected.")
        return


g1 = Graph(16)

g1.addEdge(0, 1)
g1.addEdge(0, 2)
g1.addEdge(0, 3)
g1.addEdge(3, 4)
g1.addEdge(3, 6)
g1.addEdge(3, 7)
g1.addEdge(4, 5)
g1.addEdge(4, 13)
g1.addEdge(7, 13)
g1.addEdge(8, 9)
g1.addEdge(8, 10)
g1.addEdge(11, 12)
g1.addEdge(9, 14)
g1.addEdge(9, 15)

print("\n------------- After adding the edges the graph -------\n")
print(g1)

print("\n-------------  BFS Traversal Output of the Graph with SV = 0 -------\n")
g1.BFSTraversal(sv=0)

print("\n-------------  BFS Traversal Output of the Graph with SV = 8 -------\n")
g1.BFSTraversal(sv=8)


print("\n------------- full BFS Traversal Output of the Graph -------\n")
g1.fullBFSTraversal()

print("\n------------- Graph connectivity Check using BFS traversal -------\n")
g1.isConnectedBFS()


print("\n------------- Nodes connectivity Check using BFS traversal -------\n")
g1.hasPathBFSTraversal(v1=0, v2=2)
g1.hasPathBFSTraversal(v1=0, v2=5)
g1.hasPathBFSTraversal(v1=0, v2=13)
g1.hasPathBFSTraversal(v1=0, v2=10)
g1.hasPathBFSTraversal(v1=0, v2=11)
g1.hasPathBFSTraversal(v1=8, v2=9)
g1.hasPathBFSTraversal(v1=8, v2=15)


print("\n------------- path between nodes using BFS traversal -------\n")
g1.printPathBFS(v1=0, v2=2)
g1.printPathBFS(v1=0, v2=5)
g1.printPathBFS(v1=0, v2=13)
g1.printPathBFS(v1=0, v2=10)
g1.printPathBFS(v1=0, v2=11)
g1.printPathBFS(v1=8, v2=9)
g1.printPathBFS(v1=8, v2=15)

print("\n-------------  DFS Traversal Output of the Graph with SV = 0 -------\n")
g1.DFStraversal(sv=0)
print('\n')

print("\n-------------  dFS Traversal Output of the Graph with SV = 8 -------\n")
g1.DFStraversal(sv=8)
print()


print("\n------------- full DFS Traversal Output of the Graph -------\n")
g1.fullDFStraversal()


print("\n------------- Graph connectivity Check using DFS traversal -------\n")
g1.isConnectedDFS(printnode=False)


print("\n------------- Nodes connectivity Check using BFS traversal -------\n")
g1.hasPathDFSTraversal(v1=0, v2=2)
g1.hasPathDFSTraversal(v1=0, v2=5)
g1.hasPathDFSTraversal(v1=0, v2=13)
g1.hasPathDFSTraversal(v1=0, v2=10)
g1.hasPathDFSTraversal(v1=0, v2=11)
g1.hasPathDFSTraversal(v1=8, v2=9)
g1.hasPathDFSTraversal(v1=8, v2=15)


print("\n------------- path between nodes using DFS traversal -------\n")
g1.printPathDFS(v1=0, v2=2)
g1.printPathDFS(v1=0, v2=5)
g1.printPathDFS(v1=0, v2=13)
g1.printPathDFS(v1=0, v2=10)
g1.printPathDFS(v1=0, v2=11)
g1.printPathDFS(v1=8, v2=9)
g1.printPathDFS(v1=8, v2=15)

g2 = Graph(8)

g2.addEdge(0, 1)
g2.addEdge(0, 2)
g2.addEdge(0, 3)
g2.addEdge(0, 4)
g2.addEdge(2, 5)
g2.addEdge(2, 6)
g2.addEdge(3, 6)
g2.addEdge(4, 7)
g2.addEdge(3, 7)
g2.addEdge(6, 7)

print("\n------------- After adding the edges the graph -------\n")
print(g2)

''' **** Checking all the functionalities using the BFS approach for Graph 2 *****'''

print("\n-------------  BFS Traversal Output of the Graph with SV = 0 -------\n")
g2.BFSTraversal(sv=0)

print("\n-------------  BFS Traversal Output of the Graph with SV = 8 -------\n")
g2.BFSTraversal(sv=7)


print("\n------------- full BFS Traversal Output of the Graph -------\n")
g2.fullBFSTraversal()


print("\n------------- Graph connectivity Check using BFS traversal -------\n")
g2.isConnectedBFS()


print("\n------------- Nodes connectivity Check using BFS traversal -------\n")
g2.hasPathBFSTraversal(v1=0, v2=6)
g2.hasPathBFSTraversal(v1=6, v2=4)
g2.hasPathBFSTraversal(v1=3, v2=1)
g2.hasPathBFSTraversal(v1=0, v2=7)


print("\n------------- path between nodes using BFS traversal -------\n")
g2.printPathBFS(v1=0, v2=6)
g2.printPathBFS(v1=6, v2=4)
g2.printPathBFS(v1=3, v2=1)
g2.printPathBFS(v1=0, v2=7)

print("\n-------------  DFS Traversal Output of the Graph with SV = 0 -------\n")
g2.DFStraversal(sv=0)
print('\n')

print("\n-------------  DFS Traversal Output of the Graph with SV = 8 -------\n")
g2.DFStraversal(sv=7)
print()


print("\n------------- full DFS Traversal Output of the Graph -------\n")
g2.fullDFStraversal()


print("\n------------- Graph connectivity Check using DFS traversal -------\n")
g2.isConnectedDFS(printnode=False)


print("\n------------- Nodes connectivity Check using DFS traversal -------\n")
g2.hasPathDFSTraversal(v1=0, v2=6)
g2.hasPathDFSTraversal(v1=6, v2=4)
g2.hasPathDFSTraversal(v1=3, v2=1)
g2.hasPathDFSTraversal(v1=0, v2=7)


print("\n------------- path between nodes using DFS traversal -------\n")
g2.printPathDFS(v1=0, v2=6)
g2.printPathDFS(v1=6, v2=4)
g2.printPathDFS(v1=3, v2=1)
g2.printPathDFS(v1=0, v2=7)
