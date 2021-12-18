import pytest as pt
from os import remove
import time
import funcs as fc
from funcs import find_max, find_sum, find_mult, find_min, random_arr


def run_pytests():
    args = ["-x", "tests.py"]
    pt.main(args)


def runtime_test():
    smol = 5000
    big = 100000
    data_smol = random_arr(smol, 1, 10)
    data_big = random_arr(big, 1, 10)

    start = time.time()
    find_min(data_smol)
    find_max(data_smol)
    find_sum(data_smol)
    try:
        find_mult(data_smol, flag=1)
    except:
        pass
    time_smol = time.time() - start
    print(f"Time of calculations for 5000 elems = {time_smol}")

    start = time.time()
    find_min(data_big)
    find_max(data_big)
    find_sum(data_big)
    try:
        find_mult(data_big, flag=1)
    except:
        pass
    time_big = time.time() - start
    print(f"Time of calculations for 100000 elems = {time_big}")

    print(f"---------\nRatio of the number of array elements = {big / smol}")
    print(f"Ratio of the time execution = {round(time_big / time_smol, 2)}\n---------")
    


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