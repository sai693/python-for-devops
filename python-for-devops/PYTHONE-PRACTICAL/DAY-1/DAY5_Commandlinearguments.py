#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import os

# Float variables

# Basic Arithmetic

def add(num1, num2):
    result1 = num1 + num2
    print ('Addition:', result1)
    return result1


def sub(num1, num2):
    result2 = num1 - num2
    print ('Subtraction:', result2)
    return result2


def mult(num1, num2):
    result3 = num1 * num2
    print ('Multiplication:', result3)
    return result3

def divr(num1, num2):
    result4 = num1 / num2
    print ('Division-questiont:', result4)
    return result4


def divq(num1, num2):
    result5 = num1 % num2
    print ('Division-Remainder:', result5)
    return result5


num1 = float(sys.argv[1])
operation = sys.argv[2]
num2 = float(sys.argv[3])

if operation == 'add':
    output = add(num1, num2)
    print (output)
elif operation == 'sub':
    output = sub(num1, num2)
    print (output)
elif operation == 'mult':
    output = mult(num1, num2)
    print (output)
elif operation == 'divq':
    output = divq(num1, num2)
    print (output)
elif operation == 'divr':
    output = divr(num1, num2)
    print (output)
else:
 print ("DONOT SELECTED OPERATION\n")

print(os.getenv("password"))
