#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    count = 10
    while count> 0:
        print(count)
        if count == 1:
            print("Happy New Year!")
        count -= 1
    

def square_integers(int_list):
    # code goes here!
    squared = [int_list[i]*int_list[i] for i in range(len(int_list))]
    return squared


def fizzbuzz():
    # code goes here!
    for i in range(1,101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 5 == 0:
            print("Buzz")
        elif i % 3 == 0:
            print("Fizz")
        else:
            print(i)

fizzbuzz()