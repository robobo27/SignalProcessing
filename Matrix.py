__author__ = "Robert Arnold"
import math

class Matrix:

    def __init__(self,matrix):
        """

        :rtype: Matrix
        """
        self.matrix = matrix
        self.rows = len(matrix)
        self.columns = len(matrix[0])
        for r in range(1,self.rows):
            if(len(self.matrix[r]) != self.columns):
                raise KeyError("Matrix dimensions are not the same throughout")

    def __add__(self, other):
        """
        Currently working with integer MxN matrices
        :param other Matrix:
        :return Matrix:
        """
        if (other.rows == self.rows and other.columns == self.columns):
            new = [list([]) for r in range(self.rows)]
            for row in range(self.rows):
                for col in range(self.columns):
                    new[row].append(self.matrix[row][col] + other.matrix[row][col])
            return Matrix(new)
        else:
            raise KeyError("Matrix dimensions do not match")

    def __mul__(self, other):
        None

    def __sub__(self, other):
        """
        Currently working with integer MxN matrices
        :param other Matrix:
        :return Matrix:
        """
        if (other.rows == self.rows and other.columns == self.columns):
            new = [list([]) for r in range(self.rows)]
            for row in range(self.rows):
                for col in range(self.columns):
                    new[row].append(self.matrix[row][col] - other.matrix[row][col])
            return Matrix(new)
        else:
            raise KeyError("Matrix dimensions do not match")

    def covariance(self):
        None

    def gaussJordan(self):
        None

    def determinant(self):
        None

    def inverse(self):
        None

    def transpose(self):
        new = []
        for i in range(self.columns):
            return Matrix(new.append(([row[i] for row in self.matrix])))

def main():
    new =  Matrix([[1,2,3],[1,2,3]])
    new2 = Matrix([[3,4,5],[1,2,4]])
    q = new - new2
    #print(type(q))
    return q

def printer(key,string):
    if key:
        print(string)

key = True
if __name__ == '__main__':
    print(main().matrix)

