import random
def sort(array):
    less = []
    equal = []
    greater = []

    if len(array) > 1:
        rand = random.randrange(0, len(array)-1)
        pivot = array[rand]
        for x in array:
            if x < pivot:
                less.append(x)
            if x == pivot:
                equal.append(x)
            if x > pivot:
                greater.append(x)
        # Don't forget to return something!
        return sort(less)+equal+sort(greater)  # Just use the + operator to join lists
    # Note that you want equal ^^^^^ not pivot
    else:  # You need to hande the part at the end of the recursion - when you only have one element in your array, just return the array.
        return array


print(sort([12,4,-1,5,5,6,7,3,1,15]))