#Creating a graph
#Running dijkstra's on the graph

import sys
 
class Graph(object):
    #Constructor
    def __init__(self, graphDictionary, nodes): 
        self.graph = self.fillGraph(graphDictionary, nodes)
        self.nodes = nodes
    #Fill graph with nodes and edge values
    def fillGraph(self, graphDictionary, nodes):
        graph = {}
        for node in nodes:
            graph[node] = {}
        graph.update(graphDictionary)
        for node1, edges in graph.items():
            for node2, value in edges.items():
                if graph[node2].get(node1, False) == False:
                    graph[node2][node1] = value        
        return graph
    #Returns all nodes
    def returnNodes(self):
        return self.nodes
    #Returns edges of a specific node
    def returnEdges(self, node):
        edges = []
        for neighbor in self.nodes:
            if self.graph[node].get(neighbor, False) != False:
                edges.append(neighbor)
        return edges
    #Returns value of an edge between two nodes
    def returnValue(self, node1, node2):
        return self.graph[node1][node2]

def dijkstra(graph, firstNode):
    unvisitedNodes = list(graph.returnNodes())   
    shortestPathValues = {}
    #Set distance to all nodes as infinity
    for node in unvisitedNodes:
        shortestPathValues[node] = sys.maxsize
    #Set distance to starting node as 0
    shortestPathValues[firstNode] = 0
    previousNodes = {}
    #Find the closest node and update the shortest path to it
    while unvisitedNodes:
        closestNode = unvisitedNodes[0]
        for node in unvisitedNodes:
            if shortestPathValues[node] < shortestPathValues[closestNode]:
                closestNode = node
        neighbors = graph.returnEdges(closestNode)
        for neighbor in neighbors:
            newPathLength = shortestPathValues[closestNode] + graph.returnValue(closestNode, neighbor)
            if newPathLength < shortestPathValues[neighbor]:
                shortestPathValues[neighbor] = newPathLength
                previousNodes[neighbor] = closestNode
        unvisitedNodes.remove(closestNode)
    
    return previousNodes, shortestPathValues

def display(previousNodes, graphDictionary, firstNode, lastNode):
    path = []
    node = lastNode
    
    while node != firstNode:
        path.append(node)
        node = previousNodes[node]
    
    path.append(firstNode)
    
    for i in range(0, len(path)-1):
        print(path[i] + "   -" + str(graphDictionary[path[i]][path[i+1]]) + "->   ", end ="")
    print(firstNode)

def main():
    nodes = ["A", "B", "C", "D", "E", "F", "G", "H"]
    graphDictionary = {}
    for node in nodes:
        graphDictionary[node] = {}
    
    graphDictionary["A"]["B"] = 5
    graphDictionary["A"]["D"] = 4
    graphDictionary["B"]["F"] = 1
    graphDictionary["B"]["C"] = 3
    graphDictionary["C"]["G"] = 5
    graphDictionary["C"]["H"] = 4
    graphDictionary["H"]["G"] = 1
    graphDictionary["E"]["F"] = 2
    graphDictionary["E"]["H"] = 2

    graph = Graph(graphDictionary, nodes)
    previousNodes, shortestPathValues = dijkstra(graph=graph, firstNode="A")
    
    #Display the dijksta path from A to G
    display(previousNodes, graphDictionary, firstNode="A", lastNode="G")
    
    #Console prints the path from G to A with the edge weights
if __name__ == "__main__":
    main()