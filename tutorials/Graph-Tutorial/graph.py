#!python

""" Vertex Class
A helper class for the Graph class that defines vertices and vertex neighbors.
"""


class Vertex(object):

    def __init__(self, vertex):
        """initialize a vertex and its neighbors
        neighbors: set of vertices adjacent to self,
        stored in a dictionary with key = vertex,
        value = weight of edge between self and neighbor.
        """
        self.id = vertex
        self.neighbors = {}


    def __str__(self):
        """output the list of neighbors of this vertex"""
        vertex = str(self.id)
        adjancent = str([x.id for x in self.neighbors])
        return  f"{ vertex } is adjancent to { adjancent }"


    def addNeighbor(self, vertex, weight=0):
        """add a neighbor along a weighted edge"""
        if vertex not in self.neighbors:
            self.neighbors[vertex] = weight
        else:
            raise KeyError("Vertecies are already neighbors")


    def getNeighbors(self):
        """return the neighbors of this vertex"""
        return self.neighbors.keys()


    def getId(self):
        """return the id of this vertex"""
        return self.id


    def getEdgeWeight(self, vertex):
        """return the weight of this edge"""
        return self.neighbors[vertex]


""" Graph Class
A class demonstrating the essential
facts and functionalities of graphs.
"""


class Graph:

    def __init__(self):
        """ initializes a graph object with an empty dictionary.
        """
        self.vertList = {}
        self.numVertices = 0


    def __iter__(self):
        """iterate over the vertex objects in the
        graph, to use sytax: for v in g
        """
        return iter(self.vertList.values())


    def addVertex(self, key):
        """add a new vertex object to the graph with
        the given key and return the vertex
        """
        if key in self.vertList:
            return
        
        self.numVertices += 1
        to_add = Vertex(key)
        print(to_add)
        self.vertList[key] = to_add

        return to_add


    def getVertex(self, key):
        """return the vertex if it exists"""
        return self.vertList[key]


    def addEdge(self, from_vert, to_vert, cost=0):
        """add an edge from vertex f to vertex t with a cost
        """
        if from_vert not in self.vertList:
            raise KeyError(f"{ from_vert } does not exist.")
        elif to_vert not in self.vertList:
            raise KeyError(f"{ to_vert } does not exist.")

        self.vertList[from_vert].addNeighbor(to_vert)


    def getVertices(self):
        """return all the vertices in the graph"""
        return self.vertList.keys()



# Driver code


if __name__ == "__main__":

    # Challenge 1: Create the graph

    g = Graph()

    # Add your friends
    g.addVertex("Friend 1")
    g.addVertex("Friend 2")
    g.addVertex("Friend 3")

    # ...  add all 10 including you ...

    # Add connections (non weighted edges for now)
    g.addEdge("Friend 1", "Friend 2")
    g.addEdge("Friend 2", "Friend 3")

    # Challenge 1: Output the vertices & edges
    # Print vertices
    print("The vertices are: ", g.getVertices(), "\n")

    print("The edges are: ")
    for v in g:
        print(v)
        # vertex = g.vertList[v]
        # for w in vertex.getNeighbors():
        #     print(f"( { vertex.getId() } , { w } )")
