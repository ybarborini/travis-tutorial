import numpy as np

def test_numpy_partition():
    a = np.array([3, 2, -1, 10])
    part = np.partition(a, 1)
    assert part[1] == 2
