# Authors: Amber Hankins, Nikhil Sharma
# CPE 400
# Faulty Node Analysis Project

from pyvis.network import Network

def main():
    # Create a new matrix object
    newMatrix = Matrix(3)

    # Print empty matrix
    print(newMatrix)
    
    # Adding values to the matrix (creating links between nodes)
    try:
        newMatrix.add(0, 2, 5)
        newMatrix.add(1, 2, 7)
        newMatrix.add(2, 2, 2)
        newMatrix.add(1, 1, 6)
    except:
        print("Invalid position entered for adding to matrix")
        return

    # Print newMatrix
    print(newMatrix)

    # Remove values from the matrix
    try:
        newMatrix.remove(1, 1)
    except:
        print("Invalid position entered for adding to matrix")
        return

    # Print newMatrix
    print(newMatrix)

    # Simulates pyvis graph visualizer
    net = Network()

    net.add_node(1, label='Node A')
    net.add_node(2, label='Node B')
    net.add_node(3, label='Node C')
    net.add_node(4, label='Node D')
    net.add_node(5, label='Node E')

    net.add_edge(1, 2, value=5, label="5")
    net.add_edge(1, 3, value=1, label="1")
    net.add_edge(1, 4, value=7, label="7")
    net.add_edge(1, 5, value=12, label="12")

    net.show('nodes.html')

class Matrix:
    # Initialize variables
    def __init__(self, size):
        self.size = size
        self.matrix = self.emptyMatrix()

    # This prints the matrix whenever the object is printed
    def __str__(self):
        # COnstruct a single string with desired formatting
        newString = ""
        for row in self.matrix:
            newString += "|"
            for element in row:
                newString += " " + str(element) + " "
            newString += "|\n"
        return newString

    # Create an empty matrix
    def emptyMatrix(self):
        newMatrix = []
        for i in range(self.size):
            newList = []
            for i in range(self.size):
                newList.append(0)
        # In each iteration, add an empty list to the main list
            newMatrix.append(newList)
        return newMatrix

    # Add weight to links
    def add(self, row, col, value):
        self.matrix[row][col] = value

    # Remove weight from links
    def remove(self, row, col):
        self.matrix[row][col] = 0

    def doDijikstra(self, start):
        print("")

# Ensures that the main() function is ran before anything
if __name__ == "__main__":
    main()