import random
import math
import sys
from typing import Self


"""
A custom vector class implementation for educational purposes.
"""

class Vec:
    # takes input elements which are int or float type only
    def __init__(self, src=None) -> Self:
        if src is None:
            self.elements = []
        else:
            elements = list(src)
            for x in elements:#check every element in the list to see if it is int or float
                if not isinstance(x, (int, float)):
                    raise TypeError(f"Scalar must be a number: {type(x)}")
            self.elements = elements

    def __add__(self, t: Self) -> Self:
        if not isinstance(t, Vec):
            raise TypeError(f"Expected Vec: {type(t)}") #checks for type 
        if len(self.elements) != len(t):
            raise TypeError(f"Type error - vectors must be of same dimensions")#checks for lenght of vector

        return Vec([round(x + y, 5) for x, y in zip(self.elements, t.elements)])
        # zip: pair elements
        # for: go through each pair
        # x + y: add them
        # round: round answer
        # [ ]: make a list
        # Vec: make it a vector


    def __rmul__(self, scalar: int | float) -> Self: #multiply every element of the vector and creates a new vector
        if not isinstance(scalar, (int, float)):
            raise TypeError(f"Vector multiplication with invalid type: {type(scalar)}")
        
        return Vec([round(x * scalar, 5) for x in self.elements])

    def __imul__(self, scalar: int | float) -> Self: 
        if not isinstance(scalar, (int, float)):
            raise TypeError(f"Vector multiplication with invalid type: {type(scalar)}")
        #multiply the vector by a scalar and update the existing vector
        for i, val in enumerate(self.elements):
            self.elements[i] = round(val * scalar, 5)
        return self

    def __repr__(self) -> str:
        return repr(self.elements)#shows how the vector should be displayed

    def __len__(self) -> int:
        return len(self.elements)#calculates length

    def __sub__(self, t: Self) -> Self:
        if not isinstance(t, Vec):
                    raise TypeError(f"Expected Vec: {type(t)}")#checks the type of the vec
        if len(self.elements) != len(t.elements):
            raise TypeError("Vectors must be of same dimensions")#check for same length

        return Vec([x - y for x, y in zip(self.elements, t.elements)])
        #so this creates like a zip of x and y from both the vectors and then we loop through each of the pairs of x and y and subtract the elements
        # x = 1 y =3 and then sibtract it
        #raise RuntimeError("vec subtraction unimplemented")


    def __neg__(self) -> Self:
        return Vec([-x for x in self.elements])#take each element from the vector and negate it
        #raise RuntimeError("vec negation unimplemented")

    def __radd__(self, other):
        if not isinstance(other, (int, float)):
            raise TypeError(f"Expected scalar: {type(other)}")
        return Vec([x + other for x in self.elements])# scalar + vec addition
        #raise RuntimeError("vec _radd_ unimplemented")

    def __iadd__(self, other):
        for i in range(len(self.elements)):
            self.elements[i] = round(self.elements[i] + other.elements[i], 5)
        return self
        # raise RuntimeError("vec _iadd_ unimplemented")
        # return a vector of @n zeroes. precondition: @n > 0

    @staticmethod
    def zeros(n: int) -> Self:
        v = [0] * n #creates an array of n numbers
        return Vec(v)
        # raise RuntimeError("zeros unimpleented")
        # return a vector of @n. precondition: @n > 0

    @staticmethod
    def ones(n: int) -> Self:
        v = [1] * n #creates an array of 1
        return Vec(v)
        #raise RuntimeError("ones unimpleented")
        # return a vector of @n uniformly distributed numbers in [0, 1]. precondition: @n > 0

    @staticmethod
    def uniform(n: int) -> Self:
        return Vec([random.uniform(0, 1) for _ in range(n)])
        # raise RuntimeError("random unimpleented")

    #Calculates the Euclidean norm (L2 norm) of the vector.
    # sqrt(e[0]^2 + e[1]^2 + e[2]^2 + ... + e[n-1]^2)
    def norm(self) -> float:
        return math.sqrt(sum(x * x for x in self.elements))
        # raise RuntimeError("norm unimpleented")


"""
(1) Understand the basic design of the vector abstraction. Review the implementation.
(2) Document each function.
(3) Implement all unimplemented methods.
(4) Create appropriate tests for this implementation, increasing the confidence about its correctness.
(5) Test this implementation by importing the class in a sepatate python script.

(6) Measure the performance of each of these functions on vectors of varying lengths.
    Try 2k to 64k dimension vectors and time the results.
    How would you do the measurements?
(7) Measure the performance on your machine. Check it on colab.

(8) use numpy and compare the performance.
"""


if sys.version_info < (3, 8):
    sys.exit("Error: This script requires Python 3.8 or higher.")

if __name__ == "__main__":
    z1 = Vec.zeros(5)
    print("\n zeor vector: ", z1)
    z2 = Vec.ones(3)
    print("\n unit vector: ", z2)
    v1 = Vec([0, 1, 1.03])#creating a new vector
    print("\n Creating a new vector: ",v1)
    v3 = 5 * v1 #change the multiply value from here for the rmul function
    print("\nsclar and vecotor mul: ", v3)
    # v3 *= 5
    v5 = 1 + v3 #radd 
    print("\nscalar and vector addition: ", v3)
    v2 = v1 + v3#addition of two vectors
    print("\n addition of 2 vectors: ", v2)
    v4 = v1 - v3
    print ("\n subtraction on two vectors: ", v4)
    print("\n Negation of a vector ", -(v2))

    uniform_vector = Vec.uniform(5)
    print("\n Uniform random vector:", uniform_vector)

    norm_result = v1.norm()
    print("\n Norm of Vector v1:", norm_result)

    v5 = 1 + v3
    print("\nscalar and vector addition: ", v5)

    v6 = Vec([1, 2, 3])
    v7 = Vec([4, 5, 6])

    v6 += v7
    print("\nVector after += operation: ", v6)

    v8 = Vec([1, 2, 3])
    v8 *= 5

    print("\nVector after *= operation: ", v8)