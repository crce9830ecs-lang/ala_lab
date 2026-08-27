from vec import Vec
import timeit
from vec import Vec
from numpy_vec import NumpyVec

sizes = [2000, 4000, 8000, 16000, 32000, 64000]#these are the sizes of the vectore

print("Performance Benchmark")
print("-" * 70)

for n in sizes:

    print(f"\nVector size: {n}")

    # Create vectors for custom Vec
    v1 = Vec.uniform(n)
    v2 = Vec.uniform(n)

    # Create vectors for NumPy
    np1 = NumpyVec.uniform(n)
    np2 = NumpyVec.uniform(n)

    # Custom Vec timings
    vec_add = timeit.timeit(lambda: v1 + v2, number=100)
    vec_sub = timeit.timeit(lambda: v1 - v2, number=100)
    vec_neg = timeit.timeit(lambda: -v1, number=100)
    vec_mul = timeit.timeit(lambda: 5 * v1, number=100)
    vec_radd = timeit.timeit(lambda: 5 + v1, number=100)
    vec_norm = timeit.timeit(lambda: v1.norm(), number=100)

    # NumPy timings
    numpy_add = timeit.timeit(lambda: np1 + np2, number=100)
    numpy_sub = timeit.timeit(lambda: np1 - np2, number=100)
    numpy_neg = timeit.timeit(lambda: -np1, number=100)
    numpy_mul = timeit.timeit(lambda: 5 * np1, number=100)
    numpy_radd = timeit.timeit(lambda: 5 + np1, number=100)
    numpy_norm = timeit.timeit(lambda: np1.norm(), number=100)

    print(f"{'Operation':25} {'Custom Vec':15} {'NumPy':15}")
    print("-" * 60)

    print(f"{'Addition':25} {vec_add:<15.8f} {numpy_add:<15.8f}")
    print(f"{'Subtraction':25} {vec_sub:<15.8f} {numpy_sub:<15.8f}")
    print(f"{'Negation':25} {vec_neg:<15.8f} {numpy_neg:<15.8f}")
    print(f"{'Scalar multiplication':25} {vec_mul:<15.8f} {numpy_mul:<15.8f}")
    print(f"{'Scalar + vector':25} {vec_radd:<15.8f} {numpy_radd:<15.8f}")
    print(f"{'Norm':25} {vec_norm:<15.8f} {numpy_norm:<15.8f}")