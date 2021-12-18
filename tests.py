import pytest as pt
from os import remove
import time
import funcs as fc
from funcs import find_max, find_sum, find_mult


def run_pytests():
    args = ["-x", "tests.py"]
    pt.main(args)


def runtime_test():
    data1 = [1, 2, 3, 4]
    data2 = []
    for i in range(25):
        data2 += data1
    start = time.clock()
    res = find_max(data1)
    end = time.clock()
    print(f"Time of find_max for 4 objs = {end - start}")
    start = time.time()
    res = find_max(data2)
    end = time.time()
    print(f"Time of find_max for 100 objs = {end - start}")
    start = time.time()
    res = find_mult(data1)
    end = time.time()
    print(f"Time of find_mult for 4 objs = {end - start}")
    start = time.time()
    try:
        res = find_mult(data2)
    except OverflowError:
        pass
    end = time.time()
    print(f"Time of find_mult for 100 objs = {end - start}")


def overflow_test():
    data = []
    for i in range(10000):
        data = data + [1, 2, 3, 4]
    try:
        print(fc.find_mult(data))
    except OverflowError as exc:
        print(f"Exception caught!\n{exc}")


def test_read():
    with open("deletable", "w") as f:
        f.write("1 4 2 3")
    data = fc.read_file("deletable")
    remove("deletable")
    expected = [1, 4, 2, 3]
    assert data == expected


def test_min():
    data = [10, 4, 3, 2]
    assert fc.find_min(data) == 2


def test_max():
    data = [1, 4, 3, 2]
    assert fc.find_max(data) == 4


def test_sum():
    data = [1, 4, 3, 2]
    assert fc.find_sum(data) == 10


def test_multiply():
    data = [1, 4, 3, 2]
    assert fc.find_mult(data) == 24

