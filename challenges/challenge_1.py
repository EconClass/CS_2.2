#!python

import string

DIGITS = frozenset(string.digits)

def _text_to_list(file):
    res = []
    for line in open(file):
        line.strip()
        if len(line) != 0:
            res.append(line)
    return res


def _remove_punct(string):
    res = []
    
    for char in string:
        if char in DIGITS:
            res.append(char)
    
    if len(res) > 2:
        res[2] = int(res[2])
    return res


class Vertex(object):
    """ Vertex Class
    A helper class for the Graph class that defines vertices and vertex neighbors.
    """

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
        vert = str(self.id)
        adjancent = [str(x.id) for x in self.neighbors]
        return  f"{ vert } is adjancent to { adjancent }"


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


class Graph(object):
    """ Graph Class
    A class demonstrating the essential facts and functionalities of graphs.
    """

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
            pass
            # raise KeyError("That vertex already exists.")
        
        self.num_vertices += 1
        vertex = Vertex(key)
        self.vert_dict[key] = vertex

        return vertex


    def get_vertex(self, key):
        """return the vertex if it exists"""
        return self.vert_dict[key]


    def add_edge(self, from_key, to_key, cost=0):
        """add an edge from vertex f to vertex t with a cost
        """
        if from_key not in self.vert_dict:
            raise KeyError(f"{ from_key } does not exist.")
        elif to_key not in self.vert_dict:
            raise KeyError(f"{ to_key } does not exist.")
        
        from_vert = self.vert_dict[from_key]
        to_vert = self.vert_dict[to_key]

        from_vert.add_neighbor(to_vert, cost)
        to_vert.add_neighbor(from_vert, cost)


    def get_vertices(self):
        """return all the vertices in the graph"""
        return self.vert_dict.values()


"""
Create empty graph O(1)
Populate graph with vertecies O(V)
Delegate edges between vertecies O(E)
"""


# Driver code
if __name__ == "__main__":
    import sys

    file = str(sys.argv[1])
    # file = 'small_data.txt'

    array_text = _text_to_list(file)
    # print(array_text)


    g = Graph()
    graphs = []

    for line in array_text:
        if line[0] == '(':
            verts = _remove_punct(line)
            print(*verts)
            g.add_edge(*verts)
        elif line == 'G':
            if g.num_vertices != 0:
                graphs.append(g)
            g = Graph()
        else:
            for char in line:
                if char != ',':
                    # print()
                    g.add_vertex(char)

    # print(graphs)
    '''
    create an empty list of graphs

    for each line in the text
        if the line is a "G"
            if we already have a non-empty graph
                append the graph to the list
            otherwise
                create a new empty graph
        if the line has vertecies
            add to the graph
        if the line has an edge
            add them to the graph
    '''


    # # Add your friends
    # g.add_vertex("Friend 1")
    # g.add_vertex("Friend 2")
    # g.add_vertex("Friend 3")

    # # ...  add all 10 including you ...

    # # Add connections (non weighted edges for now)
    # g.add_edge("Friend 1", "Friend 2")
    # g.add_edge("Friend 2", "Friend 3")
    # g = graphs[0]
    # print(g)
    # Challenge 1: Output the vertices & edges
    # Print vertices
    print("The vertices are: ", g.get_vertices(), "\n")
    
    print("The edges are: ")
    for v in g:
        for w in v.get_neighbors():
            print(f"( { v.get_id() } , { w } )")
