
import numpy as np


class NumpyVec:

    def __init__(self, src=None):
        if src is None:
            self.elements = np.array([], dtype=float)
        else:
            self.elements = np.array(src, dtype=float)

    def __add__(self, other):
        if not isinstance(other, NumpyVec):
            raise TypeError(f"Expected NumpyVec: {type(other)}")

        if len(self.elements) != len(other.elements):
            raise TypeError("Vectors must be of same dimensions")

        return NumpyVec(self.elements + other.elements)

    def __rmul__(self, scalar):
        if not isinstance(scalar, (int, float)):
            raise TypeError(f"Expected scalar: {type(scalar)}")

        return NumpyVec(self.elements * scalar)

    def __imul__(self, scalar):
        if not isinstance(scalar, (int, float)):
            raise TypeError(f"Expected scalar: {type(scalar)}")

        self.elements *= scalar
        return self

    def __sub__(self, other):
        if not isinstance(other, NumpyVec):
            raise TypeError(f"Expected NumpyVec: {type(other)}")

        if len(self.elements) != len(other.elements):
            raise TypeError("Vectors must be of same dimensions")

        return NumpyVec(self.elements - other.elements)

    def __neg__(self):
        return NumpyVec(-self.elements)

    def __radd__(self, scalar):
        if not isinstance(scalar, (int, float)):
            raise TypeError(f"Expected scalar: {type(scalar)}")

        return NumpyVec(self.elements + scalar)

    def __iadd__(self, other):
        if not isinstance(other, NumpyVec):
            raise TypeError(f"Expected NumpyVec: {type(other)}")

        if len(self.elements) != len(other.elements):
            raise TypeError("Vectors must be of same dimensions")

        self.elements += other.elements
        return self

    @staticmethod
    def zeros(n):
        return NumpyVec(np.zeros(n))

    @staticmethod
    def ones(n):
        return NumpyVec(np.ones(n))

    @staticmethod
    def uniform(n):
        return NumpyVec(np.random.uniform(0, 1, n))

    def norm(self):
        return np.linalg.norm(self.elements)

    def __len__(self):
        return len(self.elements)

    def __repr__(self):
        return repr(self.elements)