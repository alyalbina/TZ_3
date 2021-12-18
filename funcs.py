import sys


# read and return all data from file
def read_file(filename):
    with open(filename, "r") as f:
        data = f.read().replace("\n", " ").replace("\t", " ")
        data = data.split(" ")
        data = [x if ("," not in x) else x.replace(",", ".") for x in data]
        while 1:
            try:
                data.remove("")
            except ValueError:
                break
        try:
            data = [float(x) for x in data]
        except ValueError:
            print("[!Err] Can not read file correctly! Reset to 0")
            return [0]
        return data


def find_min(data):
    res = data[0]
    for i in data[1:]:
        if i < res:
            res = i
    return res


def find_max(data):
    res = data[0]
    for i in data[1:]:
        if i > res:
            res = i
    return res


def find_sum(data):
    summ = 0
    for i in data:
        summ += int(i)
    return summ


def find_mult(data):
    multip = 1
    for i in data:
        multip *= i
        if multip >= sys.maxsize ** 2 :
            print(f"Value {multip} creates overflow")
            raise OverflowError("Result is greater than sys.maxsize ^2!")
    return round(multip, 3)


def main_func():
    filename = ""
    while 1:
        filename = str(input("Enter name of file from which to read data: "))
        try:
            data = read_file(filename)
            break
        except FileNotFoundError:
            print("File can't be found. Try again!")

    print(f"Минимальное = {find_min(data)}")
    print(f"Максимальное = {find_max(data)}")
    print(f"Сумма = {find_sum(data)}")
    try:
        print(f"Произведение = {find_mult(data)}")
    except OverflowError:
        print("During multiplication overflow was caught!")

