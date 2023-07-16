#!/usr/bin/env python3


def happy_new_year():
    i = 10
    while i >= 0:
        print(i)
        i -= 1
    print("Happy New Year!")


def square_integers(int_list):
    square_ints = list()
    for int in int_list:
        square_int = int * int
        square_ints.append(square_int)
    return square_ints


def fizzbuzz():
    for i in range(1, 101):
        str = ""
        if i % 3 == 0:
            str += "Fizz"
        if i % 5 == 0:
            str += "Buzz"
        if str == "":
            print(i)
        else:
            print(str)
