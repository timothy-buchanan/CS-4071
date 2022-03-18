import RandomList


def randomsortedlist(length, minint, maxint):
    unsorted = RandomList.randomlist(length, minint, maxint)
    return insertionsort(unsorted)


def insertionsort(inlist):  # Function that insertion sorts a list
    if len(inlist) == 1:  # Single item in list is a sorted list
        return inlist
    else:
        element = inlist[0]
        tail = inlist[1:]
        sortedlist = insertionsort(tail)  # Recurs down into a sorted list
        for i in range(len(sortedlist)):  # Finds where element should be in the sorted list
            if element < sortedlist[i]:
                sortedlist.insert(i, element)
                return sortedlist
        sortedlist.append(element)
        return sortedlist


# Example code
# exampleList = RandomList.randomlist(10, 1, 100)
# print("Start: " + str(exampleList))
# sortedList = insertionsort(exampleList)
# print("End: " + str(sortedList))

