# Authors: Amber Hankins, Nikhil Sharma
# CPE 400
# Faulty Node Analysis Project

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

# Ensures that the main() function is ran before anything
if __name__ == "__main__":
    main()