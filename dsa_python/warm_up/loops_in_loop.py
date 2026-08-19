# for i in range(5):
#     for j in range(5):
#         print(i,j,"*")

import random


def quicksort(A, l, h, pivot_type):
    if l < h:
        q = partition(A, l, h, pivot_type)

        quicksort(A, l, q, pivot_type)
        quicksort(A, q + 1, h, pivot_type)


def partition(A, l, h, pivot_type):

    # Select pivot according to condition
    if pivot_type == "first":
        pivot_index = l

    elif pivot_type == "last":
        pivot_index = h

    elif pivot_type == "middle":
        pivot_index = (l + h) // 2

    elif pivot_type == "random":
        pivot_index = random.randint(l, h)

    else:
        raise ValueError("Invalid pivot type")

    # Move selected pivot to first position
    A[l], A[pivot_index] = A[pivot_index], A[l]

    pivot = A[l]

    i = l
    j = h

    while True:

        while A[i] < pivot:
            i += 1

        while A[j] > pivot:
            j -= 1

        if i < j:
            A[i], A[j] = A[j], A[i]

            i += 1
            j -= 1

        else:
            return j


# Original array
a = [2, 5, 1, 7, 6, 3, 4]

# Choose pivot
pivot_type = input("enter type")

quicksort(a, 0, len(a) - 1, pivot_type)

print("Pivot:", pivot_type)
print("Pivot:", pivot_type)
print("Sorted:", a)