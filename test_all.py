import numpy as np

def test_addition():
    assert 1+1 == 2

def test_division():
    assert 3./2 == 1.5

def test_partition():
    a = np.array([3, 2, -1, 10])
    part = np.partition(a, 1)
    assert part[1] == 2
