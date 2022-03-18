import InsertionSort
import math


def binarysearch(inlist, x):  # Finds x in inlist
    found = False
    low = 0
    high = len(inlist) - 1

    while not found and low <= high:
        mid = math.floor((low + high) / 2)
        if x == inlist[mid]:
            found = True
        elif x < inlist[mid]:
            high = mid - 1
        else:
            low = mid + 1

    if found:
        return str(mid)
    else:
        return "not in list"


sortedlist = InsertionSort.randomsortedlist(10, 1, 100)
print(str(sortedlist))
item = int(input("What is being searched for? "))
print("x is at index: " + binarysearch(sortedlist, item))




