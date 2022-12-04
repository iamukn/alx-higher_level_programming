#!/usr/bin/python3
# Author - IAM_UKN
import sys
from calculator_1 import add, sub, mul, div
i = sys.argv[2]
j = '*'
if (len(sys.argv) - 1 != 3):
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    sys.exit(1)
elif (i != '/' and i != '-' and i != '+' and i != '*'):
    print("Unknown operator. Available operators: +, -, * and /")
    sys.exit(1)
elif (i == '/'):
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    print("{} {} {} = {}".format(a, sys.argv[2], b, div(a, b)))
elif (i == '+'):
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    print("{} {} {} = {}".format(a, sys.argv[2], b, add(a, b)))
elif (i == '-'):
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    print("{} {} {} = {}".format(a, argv[2], b, sub(a, b)))
elif (i == j):
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    print("{} {} {} = {}".format(a, argv[2], b, mul(a, b)))
