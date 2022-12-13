# Modifying Dijkstra's Algorithm for Use in Hybrid Access Networks
## Amber Hankins, Nikhil Sharma
## Professor: Dr. Sengupta
## CPE 400: Computer Networking

### To install pyvis dependency, run:
`pip install pyvis`
### To run program:
`python3 main.py`
### Project Description

>We're going to implement a network of both wired and wireless connections. All connections will have a calculated chance of failure, with wireless connections being significantly more likely to fail. We will then implement two routing algorithms: Dijkstra's algorithm, and a modified version of Dijkstra's that also takes into account whether the node is wireless or wired. This algorithm will prefer wired connections over wireless ones in an attempt to prevent loss. We will run both these algorithms on a predefined network and see how they perform comparatively in terms of loss and "hop count", which will be determined by the preset edge lengths.

___
<br>

Abstract—Hybrid access networks employ multiple different
communication channels, allowing users to connect in a num-
ber of ways. While this can increase end-to-end transmission
speeds, these networks must account for differences between
distinct communication technologies. In a network composed of
both wireless and wired connections, it is likely that wireless
connections are less reliable than their wired counterparts. As a
result, we aim to develop a modified Dijkstra’s routing algorithm
that is biased towards wired connections, as they are less likely
to fail. Throughout this project, we create a hybrid access
network in Python. We develop a modified version of Dijkstra’s
algorithm that is biased toward wired connections. We simulate
the performance of this algorithm in our hybrid access network,
with random node failure. Finally, we analyze the performance of
this modified algorithm in comparison to the original Dijkstra’s.
Performance is measured in two metrics: loss and path length.

### Functions and Classes

#### Graph Class:
- The graph class serves as the main data structure for program functionality.

- ##### Constructor:
    - The constructor calls on the `fillGraph` function contained within the class. The constructor also stores the nodes.

- `fillGraph()`:

    - Takes the graph dictionary and nodes as parameters. Duplicates the graph data given when the graph object is initalized. It's purpose is to format the data in useable way. The data structure used is a dictionary.
- `returnNodes()`:
    - Returns the nodes in the object
- `returnEdges()`:
    - Returns the edges of a node by using the node from the parameters of this function
- `returnValue()`:
    - Return the value of an edge between two nodes as specified from the parameters.
#### `dijkstra()`:
- This function takes in the graph and starting node as the parameter and runs a commonly known dijkstra algorithm on it.

#### `dijkstraMod()`:
- This function also takes in the graph and starting node as the paramter but runs a modified version of dijkstras.
This version takes into account the transmission method of the node.
Whether a node transmits using a wireless or wired link.
It is configured so that the wired node is preferred as wired nodes are better in terms of loss.

#### `display()`:
- This function takes in many paramters including previousNodes, graphDictionary, first node, and last node.
It uses this data to output the data in a user-friendly way.
It displays the shortest path from the starting node to the ending node.
This function also contains functionality for node failures.

#### `generateVisual()`:
- This function is responsible for generating the graph visuals using the pyvis library.
It works by iterating through parameter-given data and using library functions to
generate a graph to display as an HTML file.

#### `main()`:
- The main function is the main driver. This is where the graph object is initialized with data. It calls all the other neccessary function to drive the program into it's purpose. This is also where most of the error handling occurs.

`if __name__ == "__main__": main()`:
- This line is responsible for running the `main()` function whenever the program is ran.
