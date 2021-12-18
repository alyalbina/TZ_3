from funcs import *
from tests import run_pytests, overflow_test, runtime_test


def help():
    print("1. Run calculations")
    print("2. Run tests (PyTest required)")
    print("3. Run timing tests")
    print("4. Run overflow test")
    print("0. Exit\n")


if __name__ == "__main__":
    while 1:
        print("")
        help()
        command = int(input("Choose command --> "))

        if command == 1:
            main_func()
        elif command == 2:
            run_pytests()
        elif command == 3:
            runtime_test()
        elif command == 4:
            overflow_test()
        else:
            print("Shutting down...")
            exit()
