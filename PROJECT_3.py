# -*- coding: utf-8 -*-

import sys

import argparse

import random



while True:

    k = 1

    level = input("Enter level: ")

    if level == 'exit':

        sys.exit()

    level = int(level)

    n = 10 ** level

    number1 = random.randint(0, n)

    number = int(input("Enter number: "))

    while number != number1:

        if number > number1:

            print('This number is more than the original one')

        else:

            print('This number is less than the original one')

        k += 1

        number = int(input("Enter number: "))

    print("Done!")



    file = open(f'level{level}.txt', "a")

    file.write(f'{input("Enter your name: ")} {k} {number1}' + '\n')

    file.close()

    print(" ")
