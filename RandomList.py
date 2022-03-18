import random


def randomlist(length, minint, maxint):  # Creates a random list of integers in between minint and maxint
    random.seed()
    outlist = []
    for i in range(length):
        outlist.append(random.randint(minint, maxint))
    return outlist

