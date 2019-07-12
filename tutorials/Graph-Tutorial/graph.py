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


    def add_neighbor(self, vertex, weight=0):
        """add a neighbor along a weighted edge"""
        if vertex not in self.neighbors:
            self.neighbors[vertex] = weight
        else:
            raise KeyError("Vertecies are already neighbors")


    def get_neighbors(self):
        """return the neighbors of this vertex"""
        return self.neighbors.keys()


    def get_id(self):
        """return the id of this vertex"""
        return self.id


    def get_edge_weight(self, vertex):
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
        self.vert_dict = {}
        self.num_vertices = 0


    def __iter__(self):
        """iterate over the vertex objects in the
        graph, to use sytax: for v in g
        """
        return iter(self.vert_dict.values())


    def add_vertex(self, key):
        """add a new vertex object to the graph with
        the given key and return the vertex
        """
        if key in self.vert_dict:
            return
        
        self.num_vertices += 1
        to_add = Vertex(key)
        print(to_add)
        self.vert_dict[key] = to_add

        return to_add


    def get_vertex(self, key):
        """return the vertex if it exists"""
        return self.vert_dict[key]


    def add_edge(self, from_vert, to_vert, cost=0):
        """add an edge from vertex f to vertex t with a cost
        """
        if from_vert not in self.vert_dict:
            raise KeyError(f"{ from_vert } does not exist.")
        elif to_vert not in self.vert_dict:
            raise KeyError(f"{ to_vert } does not exist.")

        self.vert_dict[from_vert].add_neighbor(to_vert)


    def get_vertices(self):
        """return all the vertices in the graph"""
        return self.vert_dict.keys()



# Driver code


if __name__ == "__main__":

    # Challenge 1: Create the graph

    g = Graph()

    # Add your friends
    g.add_vertex("Friend 1")
    g.add_vertex("Friend 2")
    g.add_vertex("Friend 3")

    # ...  add all 10 including you ...

    # Add connections (non weighted edges for now)
    g.add_edge("Friend 1", "Friend 2")
    g.add_edge("Friend 2", "Friend 3")

    # Challenge 1: Output the vertices & edges
    # Print vertices
    print("The vertices are: ", g.get_vertices(), "\n")

    print("The edges are: ")
    for v in g.vert_dict.values():
        for w in v.get_neighbors():
            print(f"( { v.get_id() } , { w } )")
