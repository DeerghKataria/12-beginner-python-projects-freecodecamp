import random
import time

# Implemention of Binary Search Algorithm:

def naive_search(l, target):
    # example l = [1, 3, 10, 12]
    for i in range(len(l)):
        if l[i] == target:
            return i
    return -1

# Binary Search uses divide and conquer!
# We will leverage the fact our list is SORTED!

def binary_search(l, target, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(l) - 1

    if low > high:  # Termination condition: If low is greater than high, the element is not in the list.
        return -1

    midpoint = (low + high) // 2  # Calculate the midpoint

    if l[midpoint] == target:
        return midpoint
    elif target < l[midpoint]:
        return binary_search(l, target, low, midpoint - 1)
    else:
        return binary_search(l, target, midpoint + 1, high)

if __name__ == '__main__':
    # l = [1, 3, 5, 10, 22]
    # target = 10
    # print(naive_search(l, target))
    # print(binary_search(l, target))

    length = 1000
    # build a sorted list
    sorted_list = set()
    while len(sorted_list) < length:
        sorted_list.add(random.randint(-3*length, 3*length))
    sorted_list = sorted(list(sorted_list))

    # To find the time duration of naive search
    start = time.time()
    for target in sorted_list:
        naive_search(sorted_list, target)
    end = time.time()
    print("Naive search time: ", (end - start)/length, "seconds")

    # To find the time duration of binary search
    start = time.time()
    for target in sorted_list:
        binary_search(sorted_list, target)
    end = time.time()
    print("Binary search time: ", (end - start)/length, "seconds")

