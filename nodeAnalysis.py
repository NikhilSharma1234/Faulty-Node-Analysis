# Authors: Amber Hankins, Nikhil Sharma
# CPE 400
# Faulty Node Analysis Project

def main():
    # Create a new matrix object
    newMatrix = Matrix(3)

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

# Ensures that the main() function is ran before anything
if __name__ == "__main__":
    main()