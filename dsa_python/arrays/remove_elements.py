def remove_element(a, n):
    # using 2 pointer
    p1 = 0
    for i in range(len(a)):
        # shift elements to left if it is not equal to n
        if a[i] != n:
            a[p1] = a[i]
            p1 = p1 + 1
    return (p1), a[:p1]

    # total unique element nums, modified array

n = 6
aa = [0, 6, 1, 1, 6, 2, 2, 4, 4, 6, 6]
print(remove_element(aa, n))

# extra-works only sorted array are there
def remove_duplicate_element_also_remove_element_that_mentioned(a, n):
    p1 = 0

    for i in range(len(a)):
        if a[i] == n:
            continue

        if a[i] != a[p1 - 1]:
            a[p1] = a[i]
            p1 += 1

    return p1, a[:p1]


n = 6
aa = [0, 0, 1, 2, 3, 3, 4, 6, 6, 7, 8]

print(remove_duplicate_element_also_remove_element_that_mentioned(aa, n))


# if there is unsorted array then use set
def remove_duplicate(a, n):
    p1 = 0
    seen = set()

    for i in range(len(a)):
        if a[i] == n:
            continue

        if a[i] not in seen:
            seen.add(a[i])
            a[p1] = a[i]
            p1 += 1

    return p1, a[:p1]

n = 6
aa = [0, 0, 6, 1, 2, 5, 9, 72, 3, 4, 4, 6, 1, 2, 6]

print(remove_duplicate(aa, n))
